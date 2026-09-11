#!/usr/bin/python3
"""Defines the FileStorage class."""

import json


class FileStorage:
    """Serialize and deserialize objects to and from a JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary containing all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add an object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize objects to the JSON file."""
        objects_dict = {}

        for key, obj in FileStorage.__objects.items():
            objects_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserialize objects from the JSON file."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                objects_dict = json.load(file)

            from models.amenity import Amenity
            from models.base_model import BaseModel
            from models.city import City
            from models.place import Place
            from models.review import Review
            from models.state import State
            from models.user import User

            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review,
            }

            for key, value in objects_dict.items():
                class_name = value.get("__class__")
                if class_name in classes:
                    FileStorage.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass
