import time
import os
"""
os
os module
operating system interfaces

This module provides a portable way of
using operating system dependent functionality.
"""

"""
os.getcwd
os.getcwd()
Return a string representing the current working directory.
"""


currentWorkingDirectory = os.getcwd()

print(currentWorkingDirectory)
# /home/treedbox
# real path of this file is:
# /home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/app.py


"""
os.mkdir
os.mkdir(path, mode=0o777, *, dir_fd=None)
Create a directory named path with numeric mode mode.

If the directory already exists, FileExistsError is raised.
"""
path = '/home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/'
createdFolder = 'createdFolder'
try:
    os.mkdir(path + createdFolder)
except Exception as e:
    print(e)
# new folder will appear in:
# /home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/created/

# or is already exists:
# [Errno 17] File exists:
# '/home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/created'

time.sleep(2)  # sleep 2 seconds

"""
os.rename
os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
Rename the file or directory src to dst. If dst is a directory,
OSError will be raised. On Unix, if dst exists and is a file,
it will be replaced silently if the user has permission.
The operation may fail on some Unix flavors if src and dst are
on different filesystems.
If successful, the renaming will be an atomic
 (this is a POSIX requirement).
 On Windows, if dst already exists,
 OSError will be raised even if it is a file.
"""
renamedFolder = 'renamedFolder'
try:
    os.rename(path + createdFolder, path + renamedFolder)
except Exception as e:
    print(e)
    # [Errno 2] No such file or directory:
    # '/home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/joni' -> '/home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/renamedFolder'


"""
os.rmdir
os.rmdir(path, *, dir_fd=None)
Remove (delete) the directory path.
Only works when the directory is empty, otherwise, OSError is raised.
In order to remove whole directory trees, shutil.rmtree() can be used.
"""

time.sleep(2)  # sleep 2 seconds

try:
    os.rename(path + renamedFolder, path + 'byeBye')
    time.sleep(.5)  # sleep 2 seconds
    os.rmdir(path + 'byeBye')
except Exception as e:
    print(e)
    # [Errno 2] No such file or directory:
    # '/home/treedbox/treedbox/dev/python/python.1.0.0/module/os/basic/renamedFolder'
