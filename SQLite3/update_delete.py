import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from os.path import abspath, realpath, join, dirname


style.use('fivethirtyeight')

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


def select_data():
    query = "SELECT * FROM %s" % (database_name)
    c.execute(query)
    for x in c.fetchall():
        print(x)


def select_where_data(column, value):
    query = "SELECT datestamp, keyword, value FROM %s WHERE %s='%s'" % (
        database_name, column, value)
    c.execute(query)

    data = c.fetchall()
    if len(data) > 0:
        for x in data:
            print(x)
    else:
        print('Nothing to show.')


def graph_data(column1, column2):
    query = "SELECT %s, %s FROM %s" % (column1, column2, database_name)
    c.execute(query)
    data = c.fetchall()

    dates = []
    values = []
    for x in data:
        print(x[0])
        date = datetime.datetime.fromtimestamp(x[0])
        dates.append(date)
        values.append(x[1])

    plt.plot_date(dates, values, '-')
    plt.show()


def update_data(column1, value1, column2, value2):
    query = "UPDATE %s SET %s='%s' WHERE %s='%s'" % (
        database_name, column1, value1, column2, value2)
    c.execute(query)
    conn.commit()
    print('Updated...................................')

    select = "SELECT * FROM %s WHERE %s='%s'" % (database_name, column1, value1)
    c.execute(select)
    data = c.fetchall()
    [print(x) for x in data]


def delete_data(column, value):
    query = "DELETE FROM %s WHERE %s='%s'" % (database_name, column, value)
    c.execute(query)
    print('Deleted...................................')

    select = "SELECT * FROM %s WHERE %s='%s'" % (database_name, column, value)
    c.execute(select)
    data = c.fetchall()
    if len(data) > 0:
        [print(x) for x in data]
    else:
        print("There's no survivor..................")


create_table('stuffToPlot')


# graph_data('unix', 'value')

# update_data('value', 999999999999, 'value', 4)

delete_data('value', 999999999999)

select_where_data('value', 999999999999)

# select_data()


c.close()
conn.close()
