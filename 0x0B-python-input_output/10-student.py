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
    def __init__(self, first_name, last_name, age):
        """Class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this function retrieves a dictionary representation
        of a Student instance"""
        # if there is no attribute or attribute isnt a list
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        
        # empty dict
        stu_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                stu_dict[attr] = getattr(self,attr)

        return stu_dict
