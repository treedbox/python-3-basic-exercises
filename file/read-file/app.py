"""Append file."""
from os.path import abspath, join, dirname

filename = 'filename.txt'
dir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

chmod = 'r'  # read
openFile = open(absFilePathAutoSlash, chmod)

read = openFile.read()
print(read)
openFile.close()
"""
Some text Lorem ipsum dolor sit amet |::|
		@treedbox
1º New bit of information
2º New bit of informationSome text Lorem ipsum dolor sit amet |::|
		@treedbox
1º New bit of information
2º New bit of informationSome text Lorem ipsum dolor sit amet |::|
		@treedbox
1º New bit of information
2º New bit of information
"""

openFile = open(absFilePathAutoSlash, chmod)
readLines = openFile.readlines()
print(readLines)
openFile.close()
"""
[
'Some text Lorem ipsum dolor sit amet |::|\n',
'\t\t@treedbox\n',
'1º New bit of information\n',
'2º New bit of informationSome text Lorem ipsum dolor sit amet |::|\n',
'\t\t@treedbox\n',
'1º New bit of information\n',
'2º New bit of informationSome text Lorem ipsum dolor sit amet |::|\n',
'\t\t@treedbox\n',
'1º New bit of information\n',
'2º New bit of information'
]
"""
