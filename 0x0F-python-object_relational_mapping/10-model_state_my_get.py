#!/usr/bin/python3
"""A script that prints the State object with the
name passed as argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    searched = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(uname, passwd, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)
    found_status = False  # not found
    for state in states:
        if state.name == searched:
            print("{}".format(state.id))
            found_status = True  # found
            break

    if found is False:
        print("Not found")
