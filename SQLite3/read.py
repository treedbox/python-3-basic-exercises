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
    unix = time.time()
    now = datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')
    query = "INSERT INTO %s (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)" % (database_name)
    c.execute(query, (unix, now, keyword, value))
    conn.commit()
    print('inseted data:', unix, now, keyword, value)


def select_data():
    query = "SELECT * FROM %s" % (database_name)
    c.execute(query)
    for x in c.fetchall():
        print(x)


def select_where_data(table, value):
    query = "SELECT datestamp, keyword, value FROM %s WHERE %s='%s'" % (database_name, table, value)
    c.execute(query)

    data = c.fetchall()
    if len(data) > 0:
        for x in data:
            print(x)
    else:
        print('Nothing to show.')


create_table('stuffToPlot')


select_data()
"""
(1540263191.850504, '2018-01-01 00:00:00', 'python', 5.0)
(1540263193.0451863, '2018-01-01 00:00:00', 'python', 9.0)
(1540263194.1342869, '2018-01-01 00:00:00', 'python', 5.0)
(1540263195.223233, '2018-01-01 00:00:00', 'python', 2.0)
(1540263196.3123515, '2018-01-01 00:00:00', 'python', 8.0)
(1540263197.3931506, '2018-01-01 00:00:00', 'python', 7.0)
(1540263198.4822464, '2018-01-01 00:00:00', 'python', 9.0)
(1540263199.7036033, '2018-01-01 00:00:00', 'python', 0.0)
"""

print('##########')
select_where_data('keyword', 'java')
# Nothing to show.

select_where_data('value', '3')
"""
('2018-01-01 00:00:00', 'python', 3.0)
('2018-01-01 00:00:00', 'python', 3.0)
('2018-01-01 00:00:00', 'python', 3.0)
('2018-01-01 00:00:00', 'python', 3.0)
('2018-01-01 00:00:00', 'python', 3.0)
('2018-01-01 00:00:00', 'python', 3.0)
('2018-10-23 00:04:12', 'python', 3.0)
('2018-10-23 00:04:14', 'python', 3.0)
('2018-10-23 00:04:15', 'python', 3.0)
"""

c.close()
conn.close()
