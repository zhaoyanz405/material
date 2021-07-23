# -*- coding: utf-8 -*-
import datetime
import socket


def parse(data):
    """

    :param data:
    :return:
    """
    _dict = {}
    if isinstance(data, bytes):
        data = data.decode('utf-8')

    pairs = data.split('\r\n')
    request_line = pairs[0].split(' ')
    _dict['method'] = request_line[0]
    _dict['url'] = request_line[1]
    _dict['http_version'] = request_line[2]
    _dict['header'] = pairs[1]

    return _dict


def handle(url):
    """

    :param url:
    :return:
    """
    if url != "/":
        status = 404
        status_msg = 'Not Found'
        content = 'oh no ! 404 happening.'
    else:
        status = 200
        status_msg = "OK"
        content = """<html><head></head><body><p class="color: red"><p/></body></html>"""

    response = "HTTP/1.1 {status} {status_msg}\nDate: {date}\n{content}".format(
        status=status, status_msg=status_msg,
        date=datetime.datetime.now(),
        content=content)

    return response.encode('utf-8')


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8086))
    s.listen()
    conn, addr = s.accept()

    buffer_size = 1024
    with conn:
        print('Connect by', addr)
        d_list = []
        while True:
            data = conn.recv(buffer_size)
            if len(data) < buffer_size:
                break

    http_data = parse(data)
    print(http_data)
    response = handle(http_data['url'])

    conn.sendall(response)
    s.close()
