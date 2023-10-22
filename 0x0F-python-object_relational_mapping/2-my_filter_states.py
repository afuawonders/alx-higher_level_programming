#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = db.cursor()
    search_name = sys.argv[4]
    query = f"SELECT * FROM states WHERE name LIKE BINARY '{search_name}'"
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
