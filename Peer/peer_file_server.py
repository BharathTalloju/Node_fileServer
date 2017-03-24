import socket

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

def sendFile(file_name, conn):

    with open('./sharedFolder'+file_name, "r")

HOST, PORT = getServerHostName()
PORT = 50002

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    data = conn.recv(5)

    if data.strip() == "fs":
        file_name = conn.recv(64)
        sendFile(file_name.strip(), conn)
