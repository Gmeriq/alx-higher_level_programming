#!/usr/bin/python3

"""List all cities from database
"""

import MySQLdb
from sys import argv

if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name {} {} {}".format(
            "FROM cities",
            "LEFT OUTER JOIN states ON cities.state_id=states.id",
            "ORDER BY cities.id ASC")
    cur.execute(query)
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
