#!/usr/bin/python3
"""Module comtains a clas Student"""


class Student:
    """Blueprint for creating students
    
    Attributes:
        first_name
        last_name
        age

    Methods:
        to_json()
    """
    first_name = ""
    last_name = ""
    age = 0


    def __init__(self, first_name, last_name, age):
        """Class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """this function retrieves a dictionary representation 
        of a Student instance"""
        return self.__dict__
