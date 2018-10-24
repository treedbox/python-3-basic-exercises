"""Append file."""
from os import getcwd
from os.path import abspath, realpath, join, dirname

content = 'Some text Lorem ipsum dolor sit amet |::|\n\t\t@treedbox'

appendMe = '\n1º New bit of information'
appendMeToo = '2º New bit of information'

filename = 'filename.txt'

dir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

chmod = 'a'  # append
openFile = open(absFilePathAutoSlash, chmod)

openFile.write(content)
openFile.write(appendMe)
openFile.write('\n')
openFile.write(appendMeToo)
openFile.close()
