import csv
import sys

def dat2csv(inputFile,outputFile,fieldnames):
	with open(inputFile,'r') as input, open(outputFile,'w') as output:
		reader = csv.DictReader(input, fieldnames=fieldnames)
		writer = csv.DictWriter(output, fieldnames=fieldnames)
		for row in reader:
			writer.writerow(row)

airline_fieldnames = ['airline_id','name','alias','iata','icao','callsign','country','active']
airport_fieldnames = ['airport_id','name','city','country','iata_faa','icao','latitude','longitude','altitude','timezone','dst', 'tz_timezone','type','source']
route_fieldnames = ['airline','airline_id','source_airport','source_airport_id','destination_airport','destination_airport_id','codeshare','stops','equipment']
dat2csv('data2/airports.dat','data2/airports.csv',airport_fieldnames)
dat2csv('data2/airlines.dat','data2/airlines.csv',airline_fieldnames)
dat2csv('data2/routes.dat','data2/routes.csv',route_fieldnames)
