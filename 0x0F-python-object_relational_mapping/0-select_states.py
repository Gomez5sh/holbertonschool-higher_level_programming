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
    cur.execute("SELECT states.id, name FROM states ORDER BY states.id ASC;")

    for dbi in cur:
        print(dbi)
else:
    pass
