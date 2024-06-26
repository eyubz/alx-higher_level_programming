#!/usr/bin/python3
""" Sql query to list all cities."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)
    curr = db.cursor()
    curr.execute("""SELECT cities.name FROM
                   cities INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (sys.argv[4], ))
    rows = curr.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    curr.close()
    db.close()
