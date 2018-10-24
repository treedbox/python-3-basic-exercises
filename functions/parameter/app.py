def example(a=10, b='foo', c=[1, 2, 3], d={'treedbox': 42}):
    print(a, b, c, d)


# default parameters
example()
# 10 foo [1, 2, 3] {'treedbox': 42}

# replacing first parameter
example('BEAR')
# BEAR foo [1, 2, 3] {'treedbox': 42}

# choose the parameter to replace
example(b='BEAR')
# 10 BEAR [1, 2, 3] {'treedbox': 42}

# replace all but one
example(1, 2, 3)
# 1 2 3 {'treedbox': 42}

# replace all
example('B', 'E', 'A', 'R')
# B E A R
