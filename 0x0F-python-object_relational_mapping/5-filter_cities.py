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
    stat = []
    cur.execute("SELECT * FROM cities\
        JOIN states ON cities.state_id = states.id\
                         ORDER BY cities.id ASC")
    for city in cur.fetchall():
        if city[4] == sys.argv[4]:
            stat.append(city[2])
    j = 1
    for i in stat:
        if j < len(stat):
            print(i, end=', ')
        elif j == len(stat):
            print(i)
        j += 1
            