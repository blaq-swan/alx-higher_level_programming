#!/usr/bin/python3
"""mysqldb connector"""


import sys
import MySQLdb


if __name__ == "__main__":
    database = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    connect = database.cursor()
    connect.execute("SELECT * FROM `states`")
    [print(state) for state in connect.fetchall()]
