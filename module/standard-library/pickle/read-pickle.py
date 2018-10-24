"""
Serialization and Deserialization module
Converte python objects to bytestream and vice versa
"""

import pickle
from os.path import abspath, realpath, join, dirname

filename = 'dict.pickle'
dir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

pickle_in = open(absFilePathAutoSlash, "rb")
example_dict = pickle.load(pickle_in)
print(example_dict)
# {1: 'Foo', 2: 'Bar', 3: 'Joni', 4: 'Treedbox'}
print(example_dict[2])
# Bar
