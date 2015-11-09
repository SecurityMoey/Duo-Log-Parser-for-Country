#!/usr/bin/env python

import sys, os

try:
    import pygeoip
except ImportError:
    print "Error: GeoIP Python Module is required and not installed. Please run 'pip install pygeoip to install"
    sys.exit()

try:
    import csv
except ImportError:
    print "Error: csv Module is required and not installed. Please run 'pip install csv' to install"
    sys.exit()

try:
    with open('/usr/local/GeoIP.dat') as file:
        pass
except IOError as e:
    print "GeoIP.dat file is not located in /usr/local.  Please obtain the file and ensure it's in the directory location. It can be found at http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz"

print "First we need to know the name of the Authentication log \n Please make sure the file is in the directory you are running this script."

sfile = raw_input("Duo Authentication Log File name: ")
ofile = r'duologswcountry.csv'
fields = ["Timestamp", "User", "IP Address"]

with open(sfile) as infile, open(ofile, "wb") as outfile:
    r = csv.DictReader(infile)
    w = csv.DictWriter(outfile, fields, extrasaction="ignore")
    w.writeheader()
    for row in r:
        w.writerow(row)

    if open(ofile) :
        pass

filename = ofile

input_file = csv.DictReader(open(ofile))

ip_add = (row["IP Address"])

def country(filename):        
    gi = pygeoip.GeoIP('/usr/local/GeoIP.dat')
    return gi.country_name_by_addr(ip_add)

with open(filename, 'rb') as handle:
    reader = csv.reader(handle)
    writer = csv.writer(open('%s.csv' % filename, 'w'))
    for row in reader:
        writer.writerow(row + [ country(row[1].strip()) ])

print r"Script Complete. Please review duologswcountry.csv to see the results"
