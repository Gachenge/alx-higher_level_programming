#!/usr/bin/python3
"""
script takes arguments
filter and print out all states starting with 'N'
order them by state.id
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
         ORDER BY states.id ASC".format(sys.argv[4]))
    for state in cursor.fetchall():
        print(state)
