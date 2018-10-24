"""Try, Try Except."""

foo = [1, 2, 3, 1, 5, 4, 5]

try:
    bar = foo.index(7)
# except Exception, e: old way
except Exception as e:
    print(e)
    # 7 is not in list

try:
    bar = foo.index(bear)  # undefined name 'bear'
# except Exception, e: old way
except Exception as e:
    print(e)
    # name 'bear' is not defined

try:
    bar = foo.index(list)
    # except Exception, e: old way
except Exception as e:
    print(e)
    # <class 'list'> is not in list


try:
    bar = foo.index(8)
except Exception as e:
    print(e)
    # 8 is not in list
else:
    bar = foo.index(boo)  # undefined name 'boo'
finally:
    print('All OK')

"""
exception ZeroDivisionError
    Raised when the second argument of a division or modulo operation
    is zero. The associated value is a string indicating the type
    of the operands and the operation.
"""


def divide(x, y):
    """Divide by zero."""
    try:
        result = x / y
    except ZeroDivisionError:
        print(ZeroDivisionError)
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(8, 2)
# result is 4.0
# executing finally clause

divide(3, 0)
# division by zero!
# executing finally clause

"""
except types:
specific except types

except NameError

except ZeroDivisionError

except Exception
"""
