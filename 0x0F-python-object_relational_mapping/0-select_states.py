#!/usr/bin/python3
"""mysqldb connector"""


from sys import argv as args
import MySQLdb as md

if __name__ == "__main__":
    db = md.connect(host="localhost", port=3306,
                    user=args[1], passwd=args[2], db=args[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM state")
    [print(state) for state in cursor.fetchall()]
