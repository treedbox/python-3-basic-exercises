"""
cx_Freeze
is a set of scripts and modules for freezing Python scripts into executables
in much the same way that py2exe and py2app do.
Unlike these two tools,
cx_Freeze is cross platform and should work on any platform
that Python itself works on. It requires Python 2.7 or higher
and does work with Python 3.

cd path/to/this/file/
python setup.py build

will be created a folder
build/
    exe.linux-x86_64-3.8/
        lib/
            ...
        distme

execute distme with
./distme
"""

from cx_Freeze import setup, Executable
from os.path import abspath, join, dirname

filename = 'distme.py'
dir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

setup(
    # options = { "build_exe": { "build_exe": "/usr/local/bin"} },
    name='Foo bar',
    version='1.0.0',
    description='Auto executable python',
    executables=[Executable(absFilePathAutoSlash)]
)
