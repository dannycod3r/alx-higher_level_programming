#!/usr/bin/python3
"""A script to contain the definition of a City model and inheried
from SQLAlchemy Base and links to the MySQL table cities
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ This class City represents a city for a MySQL database
    Attributes:
        __tablename__: table name
        id (str): The city's id.
        name (sqlalchemy.Integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
