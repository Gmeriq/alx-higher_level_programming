#!/usr/bin/python3

"""Displays according to argument"""

import MySQLdb
from sys import argv


def main():
    """Print state from argument"""

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    curs = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name='{}'ORDER BY id ASC"
    curs.execute(query.format(argv[4]))
    rstate = curs.fetchall()

    for state in rstate:
        print(state)

    curs.close()
    db.close()


if __name__ == '__main__':
    main()
