from foo import bar
import foo
"""
executable:
!/usr/bin/python
    or:
    !/usr/bin/env python

    notify linux of the path of python
    to run this script as executable on linux,
    write this line on top of the file
"""

# module
# use code as module
# foo.py:


def bar():
    print('Bar text')


def foo():
    print('Foo text')


# stop auto run
# prevent auto run
if __name__ == '__main__':
    print('it can be used like a module')

# anotherFile.py:

foo.bar()
# Bar text

foo.foo()
# Foo text

# import specific functions
# anotherFileToo.py:

bar()
# Bar text

foo.bar()
# AttributeError: 'function' object has no attribute 'foo'

foo.foo()
# AttributeError: 'function' object has no attribute 'foo'

print(foo)
# Error:
