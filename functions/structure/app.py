# create a function
def foo(arg):
    print(arg)


# call a function
foo('Hello World!')
# Hello World!


def bar(name, times):
    print('Hello', name, times, 'times!')


bar('Treedbox', 10)
# Hello Treedbox 10 times!


# function as value
def big():
    return True


bear = big()

print(bear)
# True
