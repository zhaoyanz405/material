import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8086))
s.send(b"name=test,pass=pppp")

data = s.recv(1024)
print('Received:', repr(data))
s.close()
