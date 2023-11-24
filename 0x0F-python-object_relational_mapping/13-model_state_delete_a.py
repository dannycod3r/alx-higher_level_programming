#!/usr/bin/python3
"""A script that changes the name of a State
object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(uname, passwd, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # get states that meet criteria
    states = session.query(State).filter(State.name.contains("a"))
    deleted = states.delete(synchronize_session='fetch')
    session.commit()
    session.close()
