#!/usr/bin/python2

import socket
import json
from config_details import *
from serverLog import *
from json_lib import *
from jsonmerge import merge
from pprint import pprint
from create_files_catalog import *
from os import system

def create_dummy_catalogs():
    cmd = '''echo '{"files": []}' > files_catalog.json'''
    system(cmd)
    cmd = '''echo '{"Peers":[]}' > catalog.json'''
    system(cmd)
    system(">server_debug.log")

create_dummy_catalogs()

def writeCatalog(catalog):
    """Writes the catalog to disk"""
    #convert to string
    catalog = validateAndStringifyJson(catalog)

    #write to logFile
    writeToLog(serverLogFilename, "\nMerged Catalog: \n" + catalog)

    #write to catalog_file
    with open(catalogFilename, "w") as f:
        f.write(catalog)


def mergeNewCatalog(peer_catalog):
    """merges the new 'peer_catalog' to the existing catalog"""
    try:
        #read the existing catalog into memory
        catalog = ''
        with open(catalogFilename, 'r') as catalog_file:
            catalog = catalog_file.read()
            writeToLog(serverLogFilename, __name__ + ": Read catalog: ")
            writeToLog(serverLogFilename, catalog)
            catalog = validateAndCreateJson(catalog)

        #merge the new_catalog to existing one
        for peer_index in xrange(len(catalog["Peers"])):
            if catalog["Peers"][peer_index]["id"] == peer_catalog["id"]:
                catalog["Peers"][peer_index] = peer_catalog
                break
        else:
            #if the peer is new
            catalog["Peers"].append(peer_catalog)

        #write the new catalog
        writeCatalog(catalog)

        writeToLog(serverLogFilename, "\nNew Log: " + validateAndStringifyJson(peer_catalog))
        writeToLog(serverLogFilename, "\nMerged Log: "+ validateAndStringifyJson(catalog))
        return catalog
    except ValueError as err:
        print err


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)
writeToLog(serverLogFilename, __name__ + ": Server listening at " + HOST + ":" + str(PORT))
while True:
    conn, addr = s.accept()
    writeToLog(serverLogFilename, __name__ + ": Accepted Connection from " + str(addr))

    data = ''
    while True:
        buff = conn.recv(1024)
        if not len(buff):
            break
        data += buff
    writeToLog(serverLogFilename, __name__+": Received catalog: " + data)
    catalog = mergeNewCatalog(validateAndCreateJson(data))
    files_catalog = create_files_catalog(properties['files_catalog'], catalog)
    writeToFile(properties["files_catalog"], validateAndStringifyJson(files_catalog))

    files_catalog = validateAndStringifyJson(files_catalog)
    for peer in catalog["Peers"]:
        sendPeersCatalog(files_catalog, peer["id"])

