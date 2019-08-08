import csv
import sys

def createKey():
	inputfile = 'data/routes_cutdown.csv'
	outputfile = 'data/routes_cutodown_key.csv'
	with open(inputfile,'r') as inut, open(outputfile,'w') as oput:
		r = csv.reader(inut)
		w = csv.writer(oput)
		counter = 0
		for row in r:
			counter =counter + 1
			w.writerow(row+[str(counter)])

createKey()
