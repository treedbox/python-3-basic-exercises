"""
Serialization and Deserialization module
Converte python objects to bytestream and vice versa
"""

import pickle
from os.path import abspath, realpath, join, dirname

filename = 'dict.pickle'
dir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

example_dict = {
    1: 'Foo',
    2: 'Bar',
    3: 'Joni',
    4: 'Treedbox',
}

pickle_out = open(absFilePathAutoSlash, "wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
