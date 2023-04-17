#!/usr/bin/python3
"""Takes 4 arguments and is safe from SQL injection"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    if len(argv[4]) <= 12:
        curs.execute("SELECT * FROM states WHERE BINARY name='{}'\
                ORDER BY id ASC".format(argv[4]))

        rows = curs.fetchall()
        for row in rows:
            print(row)
    curs.close()
    db.close()
