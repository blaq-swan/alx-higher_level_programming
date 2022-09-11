#!/usr/bin/python3
"""mysqldb connector"""


from sys import argv as args
import MySQLdb as md

if __name__ == "__main__":
    db = md.connect(host="localhost", port=3306,
                    user=args[1], passwd=args[2], db=args[3], charset="UTF")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cursor.fetchall()]
    cursor.close()
    db.close()
