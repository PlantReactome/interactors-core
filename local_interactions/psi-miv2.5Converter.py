import mysql.connector


def main():
	dbLoginFile = open("db_login", "r")
	user = dbLoginFile.readLine()
	password = dbLoginFile.readLine()
	host = dbLoginFile.readLine()
	database = dbLoginFile.readLine()
	
	cnx = mysql.connector.connect(user, password, host, database)
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
'-' as "Source Databases",
I.interaction_id "Interaction Identifier(s)",
'-' as "Confidence value(s)"
from Interaction I
WHERE O1.species_id = 2 OR O2.species_id = 2
left join Object O1 on I.object_id_left = O1.object_id
left join Object O2 on I.object_id_right = O2.object_id
inner join Species S1 on O1.species_id = S1.species_id
inner join Species S2 on O2.species_id = S2.species_id
left join Evidence E on I.evidence_id = E.evidence_id
limit 20
"""


#msu:loc value
#agi: 
#jgi:
	InteractionTypeMIs = ["psi-mi:\"MI:2232\"(molecular interaction)", "psi-mi:\"MI:2235\"(up-regulate)", "psi-mi:\"MI:2240\"(down-regulate)"]
	InteractorTypeMIs = ["", "", "psi-mi:\"MI:0326\"(protein)"]
	EvidenceMIs = ["", "", "psi-mi:\"MI:0045\"(Physical Interaction Evidence)", "", "", "psi-mi:\"ECO:0000008\"(Expression Pattern Evidence)"]
	IDPrefixes = ["msu", "agi", "jgi"]
	cur = cnx.cursor()
	outFile = open("data", "w")
	cur.execute(query)
	num_fields = len(cur.description)
	field_names = [i[0] for i in cur.description]
	outFile.write("\t".join(field_names) + "\n")
	rows = cur.fetchall()
	x = 0
	print(len(rows))
	for row in rows:
		line = ""
		for i, item in enumerate(row):
			value = item
			if str(value) == "None" or str(value) == "NULL":
				value = "-"
			elif x == 0 or x == 1:
				taxVal = row[x + 9]
				if taxVal == "4530":
					value = "msu:" + value
				elif taxVal == "3702":
					value = "agi:" + value
				elif taxVal == "3964":
					value = "jgi:" + value
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
			line += (str(value) + "\t")
			x = x + 1
		x = 0
		line = line + "\n"
		outFile.write(line)
main()
