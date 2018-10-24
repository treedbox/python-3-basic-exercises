import socket


# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
# <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('0.0.0.0', 0)>


host = 'pythonprogramming.net'
port = 80

# get your machine name
hostname = socket.gethostname()
print(hostname)


# get host ip
hostip = socket.gethostbyname(host)
print(hostip)
# 104.237.143.20

request = 'GET / HTTP/1.1\nHost: ' + host + '\n\n'

s.connect((host, port))
s.send(request.encode())

result = s.recv(1024)
# print(result)
"""
b'HTTP/1.1 301 Moved Permanently\r\nDate: Sun, 21 Oct 2018 19:31:01 GMT\r\nServer: Apache/2.4.10 (Ubuntu)\r\nLocation: https://pythonprogramming.net/\r\nContent-Length: 325\r\nContent-Type: text/html; charset=iso-8859-1\r\n\r\n<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\n<html><head>\n<title>301 Moved Permanently</title>\n</head><body>\n<h1>Moved Permanently</h1>\n<p>The document has moved <a href="https://pythonprogramming.net/">here</a>.</p>\n<hr>\n<address>Apache/2.4.10 (Ubuntu) Server at pythonprogramming.net Port 80</address>\n</body></html>\n'
"""

while len(result) > 0:
    print(result)
    result = s.recv(1024)
