#!/usr/bin/python2
import os.path

serverName = raw_input("Enter the server host name/ IP address: ").strip()
portId = raw_input("Enter the port number the server is bind on(31234): ").strip()
if not len(portId):
    #default portId
    portId = "31234"

with open('server.prop', 'w') as f:
    f.write(serverName + ':' + portId)
