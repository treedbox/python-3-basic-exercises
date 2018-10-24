from os.path import abspath, join, dirname
import csv

filename = 'filename.csv'
dir = abspath(dirname(__file__))
absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

with open(absFilePathAutoSlash) as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')
    print(readCSV)
    # <_csv.reader object at 0x7f95316d04b8>

    # print each row
    for row in readCSV:
        print(row)
        # ['Player Name', 'Position', 'Nicknames', 'Years Active']
        # ['Skippy Peterson', 'First Base', '"Blue Dog", "The Magician"', '1908-1913']
        # ['Bud Grimsby', 'Center Field', '"The Reaper", "Longneck"', '1910-1917']
        # ['Vic Crumb', 'Shortstop', '"Fat Vic", "Very, Very Fat Vic"', '1911-1912']

        print(row[0])
        # Vic Crumb

        print(row[1])
        # Shortstop

        print(row[0], row[1])
        # Vic Crumb Shortstop


with open(absFilePathAutoSlash) as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')

    foo = []
    bar = []
    for row in readCSV:
        a = row[0]
        b = row[1]

        foo.append(a)
        bar.append(b)

    print('foo', foo)
    # foo ['Player Name', 'Skippy Peterson', 'Bud Grimsby', 'Vic Crumb']

    print('bar', bar)
    # bar ['Position', 'First Base', 'Center Field', 'Shortstop']

    def FindNickname(arg):
        pos = 0
        find = False

        with open(absFilePathAutoSlash) as csvFile:
            """
            The with statement is used to wrap the execution of a block with
            methods defined by a context manager
            (see section With Statement Context Managers).
            This allows common try…except…finally usage patterns to be
            encapsulated for convenient reuse.
            """
            readCSV = csv.reader(csvFile, delimiter=',')

            for row in readCSV:
                if 'Nicknames' in row:
                    pos = row.index('Nicknames')
                    print('########')
                elif arg in row:
                    find = True
                    print(row[pos])

            if not find:
                foo = input('Can\'t find this name, try again: ')
                FindNickname(foo)

    bar = input('What is the Nickname of: ')
    FindNickname(bar)
