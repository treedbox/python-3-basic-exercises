import numpy as np


a = 10
b = 3
c = 10

# Addition
print(a + b)
# 13

# Subtraction
print(a - b)
# 7

# Multiplication
print(a * b)
# 30

# Division
print(a / b)
# 3.3333333333333335

# Modulo
print(a % b)
# 1

# Exponentiation
print(a ** b)
# 1000

# Floor Division
print(a // b)
# 3

# Bitwise And
print(a & b)
# 2

# Bitwise Exclusive Or
print(a ^ b)
# 9

# Bitwise Inversion
print(~a)
# -11

# Bitwise Or
print(a | b)
# 11

# Identity
print(a is b)
# False
print(a is c)
# True

# Identity
print(a is not b)
# True
print(a is not c)
# False

# Left Shift
print(a << b)
# 80

# Right Shift
print(a >> b)
# 1

# Matrix Multiplication
matrixA = np.matrix('4 2; 7 2')
matrixB = np.matrix('8 3; 5 5')
print(matrixA)
"""
[[4 2]
 [7 2]]
"""
print(matrixB)
"""
[[8 3]
 [5 5]]
"""

print(matrixA @ matrixB)
"""
[[42 22]
 [66 31]]
"""

# Negation
print(-a)
# -10

# Negation
print(not a)
# False

# Positive
print(+a)
# 10

# String Formatting
obj = {'bar': 42}
print('foo' % obj)
# foo

# Ordering
print(a > b)
# True

print(a >= b)
# True

print(a < b)
# False

print(a <= b)
# False

# Equality
print(a == b)
# False

print(a == c)
# True

# Difference
print(a != b)
# True

print(a != c)
# False
