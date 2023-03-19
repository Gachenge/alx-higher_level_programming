#!/usr/bin/python3
"""
take in argument state and output cities in that state
print and order by id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities\
        JOIN states ON cities.state_id = states.id\
                         ORDER BY cities.id ASC")
    print(", ".join([city[2] for city in cur.fetchall() if city[4] == sys.argv[4]]))
            