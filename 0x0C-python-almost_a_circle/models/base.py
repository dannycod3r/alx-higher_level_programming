#!/usr/bin/python3
"""Module supplies Base Class
"""
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV representation of list_objs to a file.

        Args:
            list_objs (list): List of instances
            (e.g., Rectangle or Square instances).

        Note:
            The filename is based on the class name (e.g., "Rectangle.csv").
        """
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = "{}.csv".format(class_name)

        # Define the field names based on the class
        field_names = cls.get_csv_field_names()

        # Open the file for writing
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)

            # Write the header row
            writer.writeheader()

            # Write the data rows
            for obj in list_objs:
                writer.writerow(obj.to_csv_dict())

    @classmethod
    def get_csv_field_names(cls):
        """Get the field names for CSV serialization.

        Returns:
            list: List of field names.
        """
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            return ["id", "size", "x", "y"]

    def to_csv_dict(self):
        """Convert instance attributes to a dictionary for CSV serialization.

        Returns:
            dict: Dictionary representing instance
            attributes for CSV serialization.
        """
        if self.__class__.__name__ == "Rectangle":
            return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        elif self.__class__.__name__ == "Square":
            return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file.

        Returns:
            list: List of instances loaded from the file.
        """
        # Get the class name
        class_name = cls.__name__

        # Build the filename
        filename = "{}.csv".format(class_name)

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                instances = []

                for row in reader:
                    # Convert CSV row to a dictionary of attributes
                    obj_dict = cls.from_csv_dict(row)

                    # Create an instance with the attributes
                    instance = cls.create(**obj_dict)
                    instances.append(instance)

                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def from_csv_dict(cls, csv_dict):
        """Convert a CSV dictionary to an instance dictionary.

        Args:
            csv_dict (dict): Dictionary representing CSV row data.

        Returns:
            dict: Dictionary representing instance attributes.
        """
        instance_dict = {}
        if cls.__name__ == "Rectangle":
            instance_dict["id"] = int(csv_dict["id"])
            instance_dict["width"] = int(csv_dict["width"])
            instance_dict["height"] = int(csv_dict["height"])
            instance_dict["x"] = int(csv_dict["x"])
            instance_dict["y"] = int(csv_dict["y"])
        elif cls.__name__ == "Square":
            instance_dict["id"] = int(csv_dict["id"])
            instance_dict["size"] = int(csv_dict["size"])
            instance_dict["x"] = int(csv_dict["x"])
            instance_dict["y"] = int(csv_dict["y"])
        return instance_dict

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw all the rectangles and squares using Turtle graphics."""
        # Create a Turtle screen
        screen = turtle.Screen()
        screen.bgcolor("white")

        # Create a Turtle object
        t = turtle.Turtle()
        t.speed(1)  # Set drawing speed (adjust as needed)

        # Function to draw a single rectangle or square
        def draw_shape(shape, color):
            t.penup()
            t.fillcolor(color)
            t.goto(shape.x, shape.y)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.forward(shape.width)
                t.left(90)
            t.end_fill()

        # Loop through the list of rectangles and draw them
        for rectangle in list_rectangles:
            draw_shape(rectangle, "blue")  # You can set your own color

        # Loop through the list of squares and draw them
        for square in list_squares:
            draw_shape(square, "red")  # You can set your own color

        # Adjust the window dimensions and coordinates
        screen.setworldcoordinates(-50, -50, 300, 300)  # Adjust as needed

        # Close the Turtle graphics window on click
        screen.exitonclick()
