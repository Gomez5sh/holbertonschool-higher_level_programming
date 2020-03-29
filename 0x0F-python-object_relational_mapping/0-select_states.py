#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if len(argv) -1 == 3:

    db = MySQLd.connect(host="localhost",
                        user=argv[1],
                        password=argv[2],
                        db=argv[3],
                        port=3306)
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY id  ASC;")

    for dbi in cur.fetchall():
        print(dbi)

    else:
        pass
