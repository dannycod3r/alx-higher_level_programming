#!/usr/bin/python3
"""Module contains class definition for State
Base - instance of declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Database model for State

    Attributes:
    __tablename__: table name
    id: state id
    name: state name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
