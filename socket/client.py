import socket

s = socket.socket()
s.connect(('127.0.0.1', 12345))

# receive data from the server
print(s.recv(1024))
s.close()
