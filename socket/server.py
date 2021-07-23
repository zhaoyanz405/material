import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8086))
s.listen()

conn, addr = s.accept()
with conn:
    print('Connect by', addr)
    d_list = []
    while True:
        data = conn.recv(1024)
        if not data:
            break

        d_list.append(data)
        conn.sendall(b"recv done.")

s.close()
