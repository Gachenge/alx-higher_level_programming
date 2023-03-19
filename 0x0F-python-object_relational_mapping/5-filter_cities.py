#!/usr/bin/python3
"""
take in argument state and outputh cities in that state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    stat = sys.argv[4]
    cur.execute("SELECT * FROM `states`")
    for state in cur.fetchall():
        if 
