#!/usr/bin/python3
"""This script contains the class definition of a City class model
and lists all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(uname, passwd, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(City.state_id == State.id).all()
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
