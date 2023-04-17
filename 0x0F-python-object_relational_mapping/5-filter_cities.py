#!/usr/bin/python3
"""Takes state as an argument and lists cities within the state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    curs = db.cursor()
    query = "SELECT cities.name FROM cities {} {} '{}' {}".format(
            "JOIN states ON cities.state_id=states.id",
            "WHERE states.name LIKE", argv[4],
            "ORDER BY cities.id ASC")
    curs.execute(query)
    data = curs.fetchall()
    cities = ", ".join(row[0] for row in data)
    print(cities)
    curs.close()
    db.close()
