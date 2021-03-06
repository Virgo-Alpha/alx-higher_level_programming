#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments:
mysql username, mysql password
and database name (no argument validation needed)"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    xCities = cur.fetchall()

    for city in xCities:
        print(city)

    cur.close()
    db.close()
