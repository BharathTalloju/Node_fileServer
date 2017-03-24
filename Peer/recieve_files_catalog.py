import socket
import sys

def getServerHostName():
    with open('server.prop') as f:
        line = f.readline().strip()
        line = line.split(':')
        line[1] = int(line[1])
        return line

def writeToFile(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return

HOST, PORT = getServerHostName()
PORT = 50001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, 50001))
s.listen(5)

while True:
    conn, addr = s.accept()
    print "Connected to ", addr
    data = ''
    buff = conn.recv(1024)
    while len(buff):
        data += buff
        buff = conn.recv(1024)
    writeToFile("files_catalog.json",data)