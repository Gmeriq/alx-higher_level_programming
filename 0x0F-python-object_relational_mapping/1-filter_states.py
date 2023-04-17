#!/usr/bin/python3

"""List states starting with N"""

import MySQLdb
from sys import argv


def main():
    """Filters by N"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    query = 'SELECT * FROM states WHERE name LIKE BINARY"N%" ORDER BY id ASC'
    curs.execute(query)
    nstates = curs.fetchall()

    for state in nstates:
        print(state)

    curs.close()
    db.close()


if __name__ == '__main__':
    main()
