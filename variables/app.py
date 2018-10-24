exampleVar = 55 + 33

exampleVar2 = print(exampleVar)
# 88

print(exampleVar)
# 88

# unpack
a, b = (2, 3)

print(a)
# 2

print(b)
# 3


c, d = 4, 5

print(c)
# 4

print(d)
# 5


e, f, big = 'foo', 'bar', 'bear'

print(e)
# foo

print(f)
# bar

print(big)
# bear

g, h = [1, 2, 3], [4, 5, 6]

print(g)
# [1, 2, 3]

print(h)
# [4, 5, 6]

i, j, k = {'foo': 32}, {'bar': 42}, {'big': 'bear'}

print(i)
# {'foo': 32}

print(j)
# {'bar': 42}

print(k)
# {'big': 'bear'}


# global variable
joni = 'treedbox'


def test1():
    print(joni)

    # joni = 'python'
    # local variable 'joni' referenced before assignment


def test2():
    global joni  # refer to a global variable inside a function
    print(joni)  # print actual value, treedbox
    joni = 'python'  # changing a global variable value
    print(joni)  # print actual value, python


test1()
# treedbox

test2()
# treedbox
# python


test1()
# python
# global variable value changed by test2()
