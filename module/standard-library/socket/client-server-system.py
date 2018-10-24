"""binding & Listening."""
import socket
import sys
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

try:
    s.bind((host, port))
except socket.error as e:
    print(e)


s.listen(5)
print('Waiting for a connection')


def thread_client(conn):
    conn.send(str.encode('Welcome, type your info\n'))

    while True:
        data = conn.recv(2048)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()


while True:
    conn, address = s.accept()
    print('Connected to:', address[0], ':', address[1])

    start_new_thread(thread_client, (conn,))
