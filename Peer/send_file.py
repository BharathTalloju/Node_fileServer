#!/usr/bin/python2

import socket
import sys

def sendFile(file_name, addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((addr, 5335))
    file_name = './sharedFolder/' + file_name
    with open(file_name) as f:
        buff = f.read(2048)

        while len(buff):
            s.send(buff)
            buff = f.read(2048)

    s.close()
    return

args = sys.argv[1:]
sendFile(args[0], args[1])