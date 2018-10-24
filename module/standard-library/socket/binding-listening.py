"""binding & Listening."""
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
port = 5555

try:
    s.bind((host, port))
except Exception as e:
    print(e)


s.listen(5)
conn, address = s.accept()

print('Connected to:', address[0], ':', address[1])

"""
on Terminal:
telnet localhost 5555
"""
