"""Port scan."""
import socket

# create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'pythonprogramming.net'


def portscan(host, port):
    """Scan port on host and return a Boolean."""
    try:
        s.connect((host, port))
        return True
    except Exception:
        return False


# test port
for x in range(20, 30):
    if portscan(host, x):
        print('Port:', x, 'is open')
    else:
        print('...', x)
