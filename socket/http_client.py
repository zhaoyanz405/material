import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8086))
s.send(b"GET / HTTP/1.1 \r\nHOST 127.0.0.1:8086\r\n")

data = s.recv(1024)
print('Received:', repr(data))
s.close()
