import socket

HOST = "0.0.0.0"  # The remote host
PORT = 500             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

s.sendall(b"hello")

data = s.recv(1024)

s.close()

print ('Received', repr(data))