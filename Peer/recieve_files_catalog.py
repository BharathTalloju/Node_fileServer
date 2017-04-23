#!/usr/bin/python2

import sys
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def writeToFile(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return

HOST= get_ip_address('wlp6s0')
PORT = 5334

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    data = ''
    buff = conn.recv(1024)
    while len(buff):
        data += buff
        buff = conn.recv(1024)
    writeToFile("files_catalog.json",data)
