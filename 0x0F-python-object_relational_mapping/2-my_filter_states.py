#!/usr/bin/python3

"""script that lists all states from the database hbtn_0e_0_usa:
Your script should take 4 arguments:
mysql username, mysql password
and database name (no argument validation needed)
state name searched"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306
                         criteria=sys.argv[4])

    cur = db.cursor()
    command = """SELECT id, name
                 FROM states
                 WHERE name LIKE BINARY {}
                 ORDER BY id ASC""".format(criteria)

    cur.execute(command)
    xStates = cur.fetchall()

    for state in xStates:
        print(state)

    cur.close()
    db.close()
