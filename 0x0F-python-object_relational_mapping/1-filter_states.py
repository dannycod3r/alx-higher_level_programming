#!/usr/bin/python3
"""
A script that lists all states with name
starting with N from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # database details from commandline
    args = sys.argv[1:]
    mysql_username = args[0]
    mysql_password = args[1]
    database_name = args[2]
    db_host = "localhost"
    port = 3306

    # connect to the database
    db = MySQLdb.connect(
        host=db_host,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=port
    )

    cur = db.cursor()
    # SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    # close connections
    cur.close()
    db.close()
