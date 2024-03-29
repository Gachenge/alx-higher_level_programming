#!/usr/bin/python3

"""
print all states in a database all arguments passed
./0-select_states.py<username, password, database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    for state in cur.fetchall():
        print(state)
