import socket

s = socket.socket()
port = 12345

# inputted an empty string makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print(f"socket binded to {port}")

s.listen(5)

while True:
    c, addr = s.accept()

    print('Got connection from', addr)

    c.send(b'Thank you for connecting\n')
    c.close()
