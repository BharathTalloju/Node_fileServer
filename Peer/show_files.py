#!/usr/bin/python2

from json_lib import *

files_catalog_name = 'files_catalog.json'

def getFilesCatalog():
    with open(files_catalog_name, "r") as f:
        files_catalog = validateAndCreateJson( f.read() )
        return files_catalog

def print_FilesList(files_catalog):
    print "%-100s %-40s" % ("FileName", "Size")
    print "-"*140
    for file_obj in files_catalog["files"]:
        print "%-100s %-40s" % (file_obj["name"], file_obj["size"])

print_FilesList(getFilesCatalog())
