import mysql.connector
import datetime
import databaseconfig as cfg
import sys
import getpass

def getopts(argv):
		opts = {}  # Empty dictionary to store key-value pairs.
		while argv:  # While there are arguments left to parse...
			if argv[0][0] == '-':  # Found a "-name value" pair.
				if len(argv) >= 2:
					if argv[1][0] != '-':
						opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
					else:
						opts[argv[0]] = ''
				else:
					opts[argv[0]] = ''
			argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
		return opts
		
def writeRowToFile(row, outFile):
	InteractionTypeMIs = ["psi-mi:\"MI:2232\"(molecular interaction)", "psi-mi:\"MI:2235\"(up-regulate)", "psi-mi:\"MI:2240\"(down-regulate)"]
	InteractorTypeMIs = ["", "", "psi-mi:\"MI:0326\"(protein)"]
	EvidenceMIs = ["", "", "psi-mi:\"MI:0045\"(Physical Interaction Evidence)", "", "", "psi-mi:\"ECO:0000008\"(Expression Pattern Evidence)"]
	line = ""
	for x, item in enumerate(row):
		value = item
		if str(value) == "None" or str(value) == "NULL" or value == None:
			value = "-"
		elif x == 0 or x == 1:
			taxVal = row[x + 9]
			if taxVal == "4530":
				value = "msu:" + value
			elif taxVal == "3702":
				value = "agi:" + value
			elif taxVal == "3964":
				value = "jgi:" + value
			elif taxVal == "39947":
				value = "stringdb:" + value
		elif x == 6:
			value = EvidenceMIs[value-1]
		elif x == 8:
			value = "pubmed:" + str(value)
		elif x == 9 or x == 10:
			value = "taxid:" + str(value)
		elif x == 11:
			value = InteractionTypeMIs[value-1]
		elif x == 13:
			value = "jaiswal:" + str(value)
		elif x == 14:
			if str(value) == "-":
				value = "intact-miscore:0.0"
			else:
				value = "intact-miscore:" + str(value)
		line += (str(value) + "\t")
	line = line + "\n"
	outFile.write(line)
	
def writeFromDB(outFile):
	# dbLoginFile = open("db_login", "r")
	# userVal = dbLoginFile.readline().rstrip('\n')
	# passwordVal = dbLoginFile.readline().rstrip('\n')
	# hostVal = dbLoginFile.readline().rstrip('\n')
	# databaseVal = dbLoginFile.readline().rstrip('\n')
	# print(userVal + '\n' + passwordVal + '\n' + hostVal + '\n' + databaseVal + '\n')
	# params = {
		# 'user': userVal, 
		# 'password': passwordVal,
		# 'host': hostVal,
		# 'database': databaseVal
	# }
	
	
	#cnx initializer removed for security
	
	cur = cnx.cursor()
	query = """select distinct
O1.object_accession "ID(s) interactor A",		
O2.object_accession "ID(s) interactor B",
'-' as "Alt. ID(s) interactor A",
'-' as "Alt. ID(s) interactor B",
'-' as "Alias(es) interactor A",
'-' as "Alias(es} interactor B",
I.evidence_code_id as "Interaction detection method(s)",
'-' as "Publication 1st author(s)",
E.source_id "Publication Identifier(s)",
S1.NCBI_taxonomy_id "Taxid Interactor A",
S2.NCBI_taxonomy_id "Taxid Interactor B",
I.interaction_type_id "Interaction Types",
'jaiswal' as "Source Databases",
I.interaction_id "Interaction Identifier(s)",
'-' as "Confidence value(s)"
from Interaction I
left join Object O1 on I.object_id_left = O1.object_id
left join Object O2 on I.object_id_right = O2.object_id
inner join Species S1 on O1.species_id = S1.species_id
inner join Species S2 on O2.species_id = S2.species_id
left join Evidence E on I.evidence_id = E.evidence_id
WHERE O1.species_id = 2 
OR O2.species_id = 2
AND I.interaction_type_id = 1
limit 100

"""
	cur.execute(query)
	rows = cur.fetchall()
	for row in rows:
		writeRowToFile(row, outFile)
	
def writeFromFile(outFile, inFile):
	row = [None] * 15
	if 'string' in str(inFile):
		next(inFile)
		for line in inFile:
			values = line.split('\t')
			tax_loc1 = values[4].split('.')
			tax_loc2 = values[5].split('.')
			row[0] = tax_loc1[1]
			row[1] = tax_loc2[1]
			row[9] = tax_loc1[0]
			row[10] = tax_loc2[0]
			row[8] = 27924014
			row[14] = values[14].split('\n')[0]
			writeRowToFile(row, outFile)


def main():
	
	
	print(sys.argv)
	
	
	opts = getopts(sys.argv)
	
	print(opts);

	
	


#msu:loc value
#agi: 
#jgi:

	
	outFile = open("data/psimi_" + datetime.datetime.now().strftime("%y-%m-%d-%H-%M") + '.tab' , "w")
	
	num_fields = 15
	field_names = ["ID(s) interactor A", "ID(s) interactor B", "Alt. ID(s) interactor A", "Alt. ID(s) interactor B", "Alias(es) interactor A", "Alias(es) interactor B", "Interaction detection method(s)", "Publication 1st author(s)",
		"Publication Identifier(s)", "Taxid Interactor A", "Taxid Interactor B", "Interaction Types", "Source Databases", "Interaction Identifier(s)", "Confidence value(s)"]
	outFile.write("\t".join(field_names) + "\n")
	if '-db' in opts.keys():
		print ("db flag true")
		writeFromDB(outFile)
	
		
		
		
	if '-f' in opts.keys():
		print('-f is true')
		fileName = opts.get('-f')
		print (fileName)
		
		inFile = open(fileName, "r")
		writeFromFile(outFile, inFile)
		
		
	
		
main()
