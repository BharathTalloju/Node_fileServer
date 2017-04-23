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

def download_file(conn,file_name):
    file_name = './sharedFolder/' + file_name
    with open(file_name, "w") as f:
        buff = conn.recv(1024)

        while len(buff):
            f.write(buff)
            buff = conn.recv(1024)
        

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = get_ip_address()
PORT = 50003

s.bind((HOST,PORT))
s.listen(5)

while True:
    conn,addr = s.accept()
    file_name = conn.recv(64).strip()
    download_file(conn, file_name)



