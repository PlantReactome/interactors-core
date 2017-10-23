import mysql.connector


def main():
	cnx = mysql.connector.connect(user='interact-read', password='pr-1nt3ract', host='floret.cgrb.oregonstate.edu', database='interaction')
	query = """select distinct 
I.object_id_left "ID(s) interactor A",		
I.object_id_right "ID(s) interactor B",
'-' as "Alt. ID(s) interactor A",
'-' as "Alt. ID(s) interactor B",
'-' as "Alias(es) interactor A",
'-' as "Alias(es} interactor B",
'-' as "Interaction detection method(s)",
'-' as "Publication 1st author(s)",
E.source_id "Publication Identifier(s)",
S1.NCBI_taxonomy_id "Taxid Interactor A",
S2.NCBI_taxonomy_id "Taxid Interactor B",
I.interaction_type_id "Interaction Types",
'-' as "Source Databases",
'-' as "Interaction Identifier(s)",
'-' as "Confidence value(s)",
'-' as "Expansion method(s)",
'-' as "Biological role(s) interactor A",
'-' as "Biological role(s) interactor B",
'-' as "Experimental role(s) interactor A",
'-' as "Experimental role(s) interactor B",
IT1.interactor_type "Type(s) interactor A",
IT2.interactor_type "Type(s) interactor B",
'-' as "Xref(s) interactor A",
'-' as "Xref(s) interactor B",
'-' as "Interaction Xref(s)",
'-' as "Annotation(s) interactor A",
'-' as "Annotation(s) interactor B",
'-' as "Interaction annotation(s)",
'-' as "Host Organism(s)",
'-' as "Interaction parameter(s)",
I.date "Creation date",
'-' as "Update date",
'-' as "Checksum(s) interactor A",
'-' as "Checksum(s) interactor B",
'-' as "Interactor Checksum(s) Negative",
'-' as "Feature(s) interactor A",
'-' as "Feature(s) interactor B",
'-' as "Stoichiometry(s) interactor A",
'-' as "Stoichiometry(s) interactor B",
'-' as "Identification method participant A",
'-' as "Identification method participant B"
from Interaction I
left join Object O1 on I.object_id_left = O1.object_id
left join Object O2 on I.object_id_right = O2.object_id
inner join Species S1 on O1.species_id = S1.species_id
inner join Species S2 on O2.species_id = S2.species_id
inner join Interactor_type IT1 on I.interactor_type_id_left = IT1.interactor_type_id
inner join Interactor_type IT2 on I.interactor_type_id_left = IT2.interactor_type_id
inner join Evidence E on I.evidence_id = E.evidence_id
limit 10
"""
	cur = cnx.cursor()
	outFile = open("data", "w")
	cur.execute(query)
	num_fields = len(cur.description)
	field_names = [i[0] for i in cur.description]
	outFile.write("\t".join(field_names) + "\n")
	rows = cur.fetchall()
	x = 0
	for row in rows:
		line = ""
		for item in row:
			value = item
			if str(value) == "None" :
				value = "-"
			if x == 8:
				value = "pubmed:" + str(value)
			elif x == 9 or x == 10:
				value = "taxid:" + str(value)
			line += (str(value) + "\t")
			x = x + 1
		x = 0
		line = line + "\n"
		outFile.write(line)
main()
