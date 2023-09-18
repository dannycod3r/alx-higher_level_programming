#!/usr/bin/python3
"""Module supplies Base Class
"""
import json


class Base:
    """Base class servers as base for all other class

    Methods:
        create - Create an instance with attributes set from a dictionary

        to_json_string - Return the JSON string representation
                            of a list of dictionaries.

        save_to_file - Write the JSON string representation of
                        list_objs to a file

        load_from_file - Load instances from a JSON file.

        from_json_string - Return a list of dictionaries from a
                            JSON string representation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Set id of instance to id or
        set to __nb_objects + 1 if id is None

        Param:
            id (int)|(None): object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries to convert to JSON.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances
            (e.g., Rectangle or Square instances).

        Note:
            The filename is based on the class name (e.g., "Rectangle.json").
        """
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = "{}.json".format(class_name)

        # Convert list_objs to a list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to a JSON string
        json_str = cls.to_json_string(list_dicts)

        # Write the JSON string to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of dictionaries from a JSON string representation.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set from a dictionary.

        Args:
            **dictionary (dict): Dictionary containing attribute values.

        Returns:
            cls: An instance of the class with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square
        else:
            dummy_instance = cls()  # Create a generic dummy instance

        # Use the update method to set attributes from the dictionary
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file.

        Returns:
            list: List of instances loaded from the file.
        """
        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = "{}.json".format(class_name)

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
