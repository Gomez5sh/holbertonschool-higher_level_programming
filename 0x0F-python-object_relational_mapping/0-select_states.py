#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb



def sqlmain(argv):

    if len(argv) -1 != 3:
        print("You must enter 3 arguments")
        return

    db = MySQLd.connect(host="localhost",
                        user=argv[1],
                        password=argv[2],
                        db=argv[3],
                        port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id  ASC;")

    for dbi in cur.fetchall():
        print(dbi)

    db.close()

if __name__=="__main__":

    import sys
    sqlmain(sys.argv)
