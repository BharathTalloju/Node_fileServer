from serverLog import *
from json_lib import *
from config_details import *
import socket

def getFilesCatalog(files_catalog_name):
    try:
        with open(files_catalog_name) as f:
            files_catalog = f.read()
            files_catalog = validateAndCreateJson(files_catalog)
            return files_catalog
    except Exception as err:
        writeToLog(serverLogFilename, __name__ +": Failed to read files catalog")

def getPeersList(files_catalog, file_name):
    peers_list = {"peers_list": []}
    for file_obj in files_catalog:
        if file_obj["name"] == file_name:
            peers_list["peers_list"] = file_obj["peers_list"]
            writeToLog(serverLogFilename, __name__ + "Obtained peers list for " + file_name + ": " + validateAndStringifyJson(peers_list))
            break

    return peers_list

def sendPeersCatalog(catalog, host):
    writeToLog(serverLogFilename, __name__ + ": Sending files catalog to" + host)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, 50001))
    s.send(catalog)
