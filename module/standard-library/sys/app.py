"""
use:
nodemon /home/treedbox/treedbox/dev/python/python.1.0.0/module/sys/basic/app.py 'Foo Bar'
or:
python /home/treedbox/treedbox/dev/python/python.1.0.0/module/sys/basic/app.py 'Foo Bar'
to run this file

sys
sys — System-specific parameters and functions
"""
import sys

"""
sys.stderr
File objects used by the interpreter for standard input, output and errors:
error message
"""

sys.stderr.write('stderr text\n')
# stderr text

sys.stderr.flush()


sys.stdout.write('stdout text\n')

filePath = sys.argv
print(filePath)
# ['/home/treedbox/treedbox/dev/python/python.1.0.0/module/sys/basic/app.py', 'Foo Bar']
