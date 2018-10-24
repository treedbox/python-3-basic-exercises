"""Scan ports."""
import socket
import threading
from queue import Queue


host = 'pythonprogramming.net'


def portscan(host, port):
    """Scan ports."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        print('>>>', port, 'is open')
        con.close()
    except Exception:
        pass
        # print('...', port)


def threader():
    """Thread generator."""
    while True:
        worker = q.get()
        portscan(host, worker)
        q.task_done()


q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 10001):
    q.put(worker)


q.join()

"""
... 27
... 26
... 24
... 23
... 19
... 8
... 17
... 18
... 4
... 13
... 9
... 7
... 20
... 14
... 10
Port 22 is open
... 22
... 5
... 21
... 15
... 11
... 16
... 28
... 12
... 2
... 3
... 6
... 25
... 1
... 29
... 30
... 31
... 41
... 39
... 37
... 40
... 36
... 35
... 34
... 38
... 52
... 50
... 42
... 47
... 51
... 49
... 55
... 44
... 54
... 33
... 45
... 56
... 48
... 32
... 46
... 43
... 53
... 57
... 58
... 59
... 60
... 72
... 68
... 71
... 70
... 67
... 66
... 69
... 64
... 65
Port 80 is open
... 80
... 62
... 63
... 81
... 77
... 76
... 75
... 78
... 86
... 82
... 74
... 84
... 79
... 83
... 85
... 73
... 87
... 61
... 88
... 89
... 90
... 93
... 92
... 91
... 96
... 95
... 98
... 94
... 97
... 100
... 99
"""
