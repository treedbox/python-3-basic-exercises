arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in arr:
    print(x)

"""
1
2
3
4
5
6
7
8
9
10
"""

for x in range(0, 10):
    print(x)
"""
0
1
2
3
4
5
6
7
8
9
"""

"""
for x in xrange(0, 10):
    print(x)

NameError: name 'xrange' is not defined

in Python 3 there is no xrange
range behaves like Python 2 xrange
"""
