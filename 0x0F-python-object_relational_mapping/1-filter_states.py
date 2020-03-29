#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=db_name,
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for dbi in cur.fetchall():
        if dbi[1][0] == 'N':
            print(dbi)

    cur.close()
    db.close()
