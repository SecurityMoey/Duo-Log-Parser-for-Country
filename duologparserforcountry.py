#!/usr/bin/env python

import csv
import os
import sys

try:
    import pygeoip
except ImportError:
    print "Error: GeoIP Python Module is not installed."
    print "Please run 'pip install pygeoip' in your virtualenv."
    sys.exit()

try:
    with open('/usr/local/GeoIP.dat') as file:
        pass
except IOError as e:
    print "'GeoIP.dat' is not located in /usr/local"
    print "Please obtain the file and ensure it's in the directory location."
    print "It can be found at the following URL:"
    print "https://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz"
    sys.exit()

print "First we need to know the name of the Authentication log"
print "Please make sure the file is in the directory you are running this script."

sfile = raw_input("Duo Authentication Log File name: ")
ofile = 'duologswcountry'
fields = ["Timestamp", "User", "IP Address"]

with open(sfile, "rb") as infile, open(ofile, "wb") as outfile:
    r = csv.DictReader(infile)
    w = csv.DictWriter(outfile, fields, extrasaction="ignore")
    w.writeheader()
    for row in r:
        w.writerow(row)

input_file = csv.DictReader(open(ofile))

gi = pygeoip.GeoIP('/usr/local/GeoIP.dat')

def country(addr):
    return gi.country_name_by_addr(addr)

with open(ofile, 'rb') as handle:
    reader = csv.reader(handle)
    writer = csv.writer(open('%s.csv' % ofile, 'w'))
    for row in reader:
        addr = int(row['IP Address'])
        writer.writerow(row + [ country(addr) ])

print "Script Complete."
print "Please review duologswcountry.csv to see the results"
