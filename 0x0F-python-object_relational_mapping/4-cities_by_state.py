#!/usr/bin/python3

"""List all cities from database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    query = "SELECT cities.id, cities.name, states.name {} {} {}".format(
            "FROM cities",
            "INNER JOIN states ON cities.states_id=states.id",
            "ORDER BY cities.id ASC")
    
    curs.execute(query)
    data = curs.fetchall()
    for row in data:
        print(row)
    curs.close()
    db.close()
