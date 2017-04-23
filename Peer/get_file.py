#!/usr/bin/python2

import socket
import sys
from  json_lib import *

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def get_peersList_file(file_name):
    files_catalog = None
    peers_list  = None
    with open('files_catalog_', "r") as f:
        files_catalog = validateAndCreateJson(f.read())

    for file_obj in files_catalog:
        if file_obj["name"] == file_name:
            peers_list = file_obj["peers_list"]
            break
    return peers_list

def get_file(file_name):
    peers_list  = get_peersList_file(file_name)
    addr = peers_list[0]
    file_name = file_name + " "*(64 - len(file_name))
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((addr, 50002))

    s.send(file_name)
    s.close()
    return


args = sys.argv[1:]
get_file(args[0])
