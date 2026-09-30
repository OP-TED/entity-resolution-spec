# Quick script to find similar names from name1, name2 in same-as-orgs.tsv

from difflib import SequenceMatcher
import csv
import sys

def similar(a, b):
		return SequenceMatcher(None, a, b).ratio()

reader = csv.DictReader(sys.stdin, delimiter='\t')
headers = reader.fieldnames + ['similarity']
new_rows = []
for row in reader:
	name1 = row['name1']
	name2 = row['name2']

	sim = similar(name1, name2) if name1 and name2 else 0.0

	# Make the new row as a plain array
	new_row = [row[col] for col in headers[:-1]] + [str(sim)]
	new_rows.append(new_row)


new_rows = sorted(new_rows, key=lambda x: x[-1], reverse=True)

# Reprint it as a new TSV
writer = csv.writer(sys.stdout, delimiter='\t')
writer.writerow(headers)
for row in new_rows:
	writer.writerow(row)
