import socket


def parse(data):
    """

    :param data:
    :return:
    """
    _dict = {}

    data = data.decode('utf-8')
    for pairs in data.split(','):
        k, v = pairs.split('=')
        _dict[k] = v

    return _dict


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

        print(parse(data))
        d_list.append(data)
        conn.sendall(b"recv done.")

s.close()
