#!/usr/bin/python3

""" Connect to database """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    curs = db.cursor()
    curs.execute('SELECT* FROM states ORDER BY id ASC')
    states = curs.fetchall()
    for state in states:
        print(state)

    curs.close()
    db.close()
