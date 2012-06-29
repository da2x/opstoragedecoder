#!/usr/bin/env python
from xml.dom.minidom import *
from base64 import *
import sys

def pad(string, length=50, padchar=" "):
	return string + padchar * (length-len(string))

def getDecodedElementTextNode(entry, elem):
	try:
		value = entry.getElementsByTagName(elem)
		value = value[0].childNodes[0].data
		return b64decode(value).decode("UTF-16")
	except:
		return "nil" # represents literal value

if not len(sys.argv) == 2:
 	print "Prints a human-readable presentation of the encoded contents in a persistent storage (pstorage) database file used by Opera."
	print "\tUsage: `./opstoragedecoder.py <file>`"
	sys.exit(1)

document = sys.argv[1]
entries = parse(document).getElementsByTagName("e")
data = { getDecodedElementTextNode(entry, "k") : getDecodedElementTextNode(entry, "v") for entry in entries }

for key,value in data.items():
	print pad(key) + value
