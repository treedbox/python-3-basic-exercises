# list
# list is mutable
# array-like

# generate slower than tuple
# iterate slower than tuple

foo = [1, 2, 3, 4, 5]

foo.append(6)
print(foo)
# [1, 2, 3, 4, 5, 6]

# list insert
# .insert(position, value)
# insert between 2 and 3
foo.insert(2, 99)
print(foo)
# [1, 2, 99, 3, 4, 5, 6]

foo.remove(2)
print(foo)
# [1, 99, 3, 4, 5, 6]
# can't remove what is inserted above


print(foo[2])
# 3

# slice
# slice from to
print(foo[2:4])
# [3, 4]

print(foo[-3:-1])
# [4, 5]

# last element

print(foo[-1])
# 6

# index
# index of
# return the position of the first elements that matchs
print(foo.index(3))
# 2
bar = [1, 2, 3, 1, 5, 4, 5]
# ignore the last element
print(bar.index(5))
# 4


# count
# how many occurrences
print(bar.count(5))
# 2

# list sort
# sort numbers
bar.sort()
print(bar)
# [1, 1, 2, 3, 4, 5, 5]

# sort strings
bear = ['joni', 'treedbox', 'google', 'dev']
bear.sort()
print(bear)
# ['dev', 'google', 'joni', 'treedbox']


# boolean if element exists in list
exists = 'joni' in bear
notExists = 'foo' in bear

print(exists)
# True
print(notExists)
# False

"""
In your example, if you print x.index(2) it will only give the first index.
You can specify from where to start search (x.index(2,3) means it will search
for 2 from the 3 index) and where to end (x.index(2,3,7) will search for 2
between the 3rd and 7th indexes). And you can create a list of indexes of any
object using a loop.﻿
"""
