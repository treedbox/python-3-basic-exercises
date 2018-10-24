from ftplib import FTP
from os.path import abspath, join, dirname

host = 'your.com'
user = 'youlogin'
password = 'yourpass'
remotedir = '/folder/on/server/'

filename = 'file.txt'
localdir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

ftp = FTP(host)
ftp.login(user=user, passwd=password)
ftp.cwd(remotedir)


# Download
# RETR Retrieve a copy of the file
# wb = write + binary mode
# 1024 = buffer size
def retrFile(file):
    with open(file, 'wb') as local_file:
        ftp.retrbinary('RETR ' + filename, local_file.write)
    ftp.quit()


# Upload
# STOR Accept the data and to store the data as a file at the server site
# wb = read + binary mode
# 1024 = buffer size
def storFile(file):
    with open(file, 'rb') as fobj:
        ftp.storbinary('STOR ' + filename, fobj, 1024)
    ftp.quit()

# Upload
# storFile(absFilePathAutoSlash)


# Download
retrFile(absFilePathAutoSlash)

"""
ftplib.error_perm: 530 Login authentication failed

"""
