#!/usr/bin/python3
"""
A script that lists all states with name
same as searched state from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # database details from commandline
    args = sys.argv[1:]
    mysql_username = args[0]
    mysql_password = args[1]
    database_name = args[2]
    state_name = args[3]
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
    cur.execute("SELECT cities.id, cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name LIKE BINARY %s \
                 ORDER BY cities.name ASC", (state_name,))
    cities_fetched = cur.fetchall()

    if cities_fetched is not None:
        print(", ".join([row[1] for row in cities_fetched]))

    # close connections
    cur.close()
    db.close()
