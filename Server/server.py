import socket
import json
from jsonmerge import merge
from pprint import pprint

catalogFilename = 'catalog.json'
serverLogFilename = 'server_log.log'
PORT = 5000
HOST = ''


def writeToLog(fileName, data):
    with open(fileName,'a') as logFile:
        logFile.write(data)

def validateAndStringifyJson(data):
    try:
        return json.dumps(data, indent=4)
    except NameError as err:
        print "Error stringifying the json object, skipping."
        return None

def validateAndCreateJson(data):
    try:
        return json.loads(data)
    except ValueError as err:
        print "Error creating the json, skipping."

def writeCatalog(catalog):
    #convert to string
    catalog = validateAndStringifyJson(catalog)

    #write to logFile
    writeToLog(serverLogFilename, "\nMerged Catalog: \n" + catalog)

    #write to catalog_file
    with open(catalogFilename, "w") as f:
        f.write(catalog)


def mergeNewCatalog(peer_catalog):
    try:
        #read the existing catalog into memory
        catalog = ''
        with open(catalogFilename, 'r') as catalog_file:
            catalog = catalog_file.read()
            writeToLog(serverLogFilename, "\n\n\nRead catalog: ")
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
    except ValueError as err:
        print err


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(5)
while True:
    conn, addr = s.accept()
    print addr, "Connected"

    data = ''
    while True:
        buff = conn.recv(1024)
        if not buff:
            break
        data += buff

    mergeNewCatalog(validateAndCreateJson(data))
