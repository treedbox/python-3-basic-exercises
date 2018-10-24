a = -5
b = 5

"""
abs
abs(x)
Return the absolute value of a number.
The argument may be an integer or a floating point number.
If the argument is a complex number, its magnitude is returned.
"""

print(abs(a))
# 5

compare = abs(a) == b

print(compare)
# True

"""
help
help([object])
Invoke the built-in help system.
(This function is intended for interactive use.)

If no argument is given,
the interactive help system starts on the interpreter console.
If the argument is a string,
then the string is looked up as the name of a module, function, class,
method, keyword, or documentation topic,
and a help page is printed on the console.

If the argument is any other kind of object,
a help page on the object is generated.

This function is added to the built-in namespace by the site module.

Changed in version 3.4:
Changes to pydoc and inspect mean that the reported signatures for callables
are now more comprehensive and consistent.
"""
help('time')
# show documentation about time

"""
max
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
Return the largest item in an iterable or the largest of two or more arguments.
"""
list = [4, 46, 546, 3, 57, 895, 4]
print(max(list))
# 895

"""
min
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
Return the smallest item in an iterable or the smallest of two or more arguments
"""
print(min(list))
# 3

"""
round
round(number[, ndigits])

5.5: round to up. will ceil to 6
5.4: round to down will floor to 5
Return number rounded to ndigits precision after the decimal point.
If ndigits is omitted or is None, it returns the nearest integer to its input.
"""

c = 5.5
d = 5.4

print(round(c))
# 6
print(round(d))
# 4

# int
# string to int
e = '55'
print(int(e) + 1)
# 56

# str
# int to string
f = 32
print(str(f) + ' Text')
# 32 Text


# float
# int to float
# string to float
g = 43
print(float(g))
# 43.0

h = '43'
print(float(g))
# 43.0
