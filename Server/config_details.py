#!/usr/bin/python2

import socket
import fcntl
import struct
from serverLog import *
from json_lib import *

catalogFilename = "catalog.json"
PORT = 5000
propertiesFilename = "properties.json"
files_catalog_name = "files_catalog.json"

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def updatePropertiesFile(**kwargs):
    properties = dict()

    if kwargs:
        for key in kwargs:
            properties[key] = str(kwargs[key])
            pass
        writeToFile(propertiesFilename, validateAndStringifyJson(properties))
        pass



def getHostName():
    HOST = get_ip_address('wlp6s0')
    return HOST

HOST = getHostName()
if __name__ == '__main__':

    HOST=getHostName()
    s_port = raw_input("Enter the port you want to listen to(5000)").strip()
    if not len(s_port):
        s_port = '5000'
    try:
        PORT = int(s_port)
        writeToLog(serverLogFilename, "Switching port to" + s_port)
    except ValueError as err:
        writeToLog(serverLogFilename, "invalid port number entered: " +s_port +", " + str(err) + "\nswitching todefault port 5000")
        PORT = 5000
    r_i = raw_input("Enter a name for the catalog file(catalog.json): ").strip()
    if len(r_i):
        catalogFilename = r_i

    #read the filesCatalog file name
    r_i =raw_input("name of the files catalog file(files_catalog.json): ").strip()
    if len(r_i):
        files_catalog=r_i

    writeToLog(serverLogFilename, "Updating properties file")
    updatePropertiesFile(HOST=HOST, PORT=PORT, catalogFilename=catalogFilename, files_catalog=files_catalog)
