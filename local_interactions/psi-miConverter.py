import mysql.connector


def main():
	cnx = mysql.connector.connect(user='interact-read', password='pr-1nt3ract', host='floret.cgrb.oregonstate.edu', database='interaction')
	query = """select 
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
'-' as "Interaction Identifier(s)",
'-' as "Confidence value(s)",
'-' as "Expansion method(s)",
'-' as "Biological role(s) interactor A",
'-' as "Biological role(s) interactor B",
'-' as "Experimental role(s) interactor A",
'-' as "Experimental role(s) interactor B",
I.interactor_type_id_left "Type(s) interactor A",
I.interactor_type_id_right "Type(s) interactor B",
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
'-' as "Identification method participant B",
S1.species "Species name",
S2.species "Species name"
from Interaction I
left join Object O1 on I.object_id_left = O1.object_id
left join Object O2 on I.object_id_right = O2.object_id
inner join Species S1 on O1.species_id = S1.species_id
inner join Species S2 on O2.species_id = S2.species_id
left join Evidence E on I.evidence_id = E.evidence_id
"""

	InteractionTypeMIs = ["psi-mi:\"MI:2232\"(molecular interaction)", "psi-mi:\"MI:2235\"(up-regulate)", "psi-mi:\"MI:2240\"(down-regulate)"]
	InteractorTypeMIs = ["", "", "psi-mi:\"MI:0326\"(protein)"]
	EvidenceMIs = ["", "", "psi-mi:\"MI:0045\"(Physical Interaction Evidence)", "", "", "psi-mi:\"ECO:0000008\"(Expression Pattern Evidence)"]
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
			elif x == 6:
				value = EvidenceMIs[value-1]
			elif x == 8:
				value = "pubmed:" + str(value)
			elif x == 9 or x == 10:
				value = "taxid:" + str(value) + "(" + row[x + 32] + ")"
			elif x == 11:
				value = InteractionTypeMIs[value-1]
			elif x == 20 or x == 21:
				value = str(InteractorTypeMIs[int(value)-1])
			elif x == 30:
				value = "/".join(value.split('-'))
			line += (str(value) + "\t")
			x = x + 1
			if i == 40:
				break
		x = 0
		line = line + "\n"
		outFile.write(line)
main()
