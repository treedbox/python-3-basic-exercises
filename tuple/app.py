"""Tuple"""
# tuple is imutable
# generate faster than list
# iterate faster than list

foo = 1, 2, 3, 4, 1

bar = (1, 2, 3, 4, 1)


def bear():
    return 1, 2


a, b = bear()

print(a)
# 1

print(b)
# 2

print(foo)
# (1, 2, 3, 4, 1)

print(bar)
# (1, 2, 3, 4, 1)

print(foo[1])
# 2

print(bar[1])
# 2

print(1, 2, 3)
# 1 2 3
# it's not a tuple

# foo[1] = 3
# TypeError: 'tuple' object does not support item assignment

# bar[1] = 3
# TypeError: 'tuple' object does not support item assignment
