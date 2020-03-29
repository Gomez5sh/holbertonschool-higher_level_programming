#!/usr/bin/python3
"""lists all states with a name starting with N"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for dbi in cur.fetchall():
        print(dbi)

    cur.close()
    db.close()
