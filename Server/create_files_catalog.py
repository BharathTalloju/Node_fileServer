#!/usr/bin/python2

from serverLog import *
from config_details import *
from json_lib import *
from send_peer_list import *

def getConfigProperties():
    properties = ''
    try:
        with open(propertiesFilename, "r") as f:
            properties = f.read()
            properties = validateAndCreateJson(properties)
            return properties
    except Exception as err:
        writeToLog(serverLogFilename, "Error reading properties file")

properties = getConfigProperties()

def getCatalog():
    catalog = None
    try:
        with open(properties['catalogFilename'], "r") as catalog_file:
            catalog = validateAndCreateJson( catalog_file.read() )
    except Exception as err:
        writeToLog(serverLogFilename,"Error reading the catalog file")

    return catalog

def getFilesCatalog():
    files_catalog = None

    try:
        with open(properties['filesCatalogFilename'], "r") as f:
            files_catalog = validateAndCreateJson( f.read() )
    except Exception as err:
        writeToLog(serverLogFilename, "Error reading files catalog")

    return files_catalog


def create_files_catalog(files_catalog_filename, catalog):
    files_catalog = dict({"files": []})
    for peer in catalog["Peers"]:
        for file_obj in peer["files"]:
            for file_obj2 in files_catalog["files"]:
                if file_obj["name"] == file_obj2["name"]:
                    file_obj2["peers_list"].append(peer["id"])
                    break
            else:
                new_file_obj = dict()
                new_file_obj["name"] = file_obj["name"]
                new_file_obj["size"] = file_obj["size"]
                new_file_obj["peers_list"] = [peer["id"]]
                files_catalog["files"].append(new_file_obj)
                pass
            pass
        pass

    writeToLog(serverLogFilename, "files catalog created" + validateAndStringifyJson(files_catalog))
    return files_catalog


# catalog = getCatalog()
# files_catalog = create_files_catalog(properties['files_catalog'], catalog)

# writeToFile(properties["files_catalog"], validateAndStringifyJson(files_catalog))

# files_catalog = validateAndStringifyJson(files_catalog)
# for peer in catalog["Peers"]:
#     sendPeersCatalog(files_catalog, peer["id"])


