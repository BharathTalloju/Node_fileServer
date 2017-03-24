import socket

def getServerHostName():
    with open('server.prop') as f:
        line = f.readline().strip()
        print "Read: ", line
        line = line.split(':')
        line[1] = int(line[1])
        return line

catalog_file_path = './catalog.json'
HOST, PORT = getServerHostName()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST, PORT))

with open(catalog_file_path, 'r') as f:
    buffer = f.read()
    print "Read catalog: ", buffer
    s.send(buffer)
