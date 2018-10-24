import sqlite3
import time
import datetime
import random
from os.path import abspath, realpath, join, dirname


database = 'tutorial.db'

dir = abspath(dirname(__file__))
absFilePathDatabase = abspath(join(dirname(__file__), database))

database_name = ''
conn = sqlite3.connect(absFilePathDatabase)
c = conn.cursor()


def create_table(name):
    global database_name
    database_name = name
    """Create a database."""
    query = "CREATE TABLE IF NOT EXISTS %s(unix REAL, datestamp TEXT, keyword TEXT, value REAL)" % (
        database_name)
    c.execute(query)


def insert_data(keyword, value):
    """Insert data."""
    conn = sqlite3.connect(absFilePathDatabase)
    c = conn.cursor()
    unix = time.time()
    now = datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO %s (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)" % (database_name)
    c.execute(query, (unix, now, keyword, value))
    conn.commit()
    print('inseted data:', unix, now, keyword, value)


create_table('stuffToPlot')


for x in range(10):
    insert_data('python', random.randrange(0, 10))
    time.sleep(1)
c.close()
conn.close()


"""
REAL = floar
TEXT = string
"""
