import socket
#import string
HOST = 'localhost'
PORT = 11719
st = 'broadcast!'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while 1:
    sock.sendto(st.encode('utf8'),(HOST,PORT))