"""
subprocess
Allows you to spawn new processes,
connect to their input/output/error pipes,
and obtain their return codes.
"""
import subprocess

# windows
# subprocess.call('dir', shell=True)
# linux
subprocess.call('ls', shell=True)

output = subprocess.check_output('ls', shell=True)
print(output)


subprocess.call('python foo.py', shell=True)
# Foo
# from foo.py
subprocess.call('python systut.py "Lorem Ipsum "', shell=True)

# execute commands
subprocess.call('sudo apt-get install treedbox', shell=True)
