#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import unittest
import uuid
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel."""

    def test_id_is_string(self):
        """Test that id is a string."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_id_is_unique(self):
        """Test that each instance has a unique id."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_id_is_valid_uuid(self):
        """Test that id is a valid UUID."""
        model = BaseModel()
        uuid_obj = uuid.UUID(model.id)
        self.assertEqual(str(uuid_obj), model.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_created_at_and_updated_at_are_set(self):
        """Test that creation and update times are initialized."""
        model = BaseModel()
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertGreaterEqual(model.updated_at, old_updated_at)

    def test_save_does_not_change_id(self):
        """Test that save does not change the id."""
        model = BaseModel()
        old_id = model.id
        model.save()
        self.assertEqual(model.id, old_id)

    def test_str(self):
        """Test the string representation."""
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected)

    def test_to_dict_returns_dictionary(self):
        """Test that to_dict returns a dictionary."""
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_to_dict_contains_class(self):
        """Test that __class__ is included."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["__class__"], "BaseModel")

    def test_to_dict_contains_id(self):
        """Test that id is included."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["id"], model.id)

    def test_to_dict_contains_dates_as_strings(self):
        """Test that dates are converted to ISO strings."""
        model = BaseModel()
        obj_dict = model.to_dict()

        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

    def test_to_dict_date_format(self):
        """Test that dates use ISO format."""
        model = BaseModel()
        obj_dict = model.to_dict()

        self.assertEqual(
            obj_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(
            obj_dict["updated_at"], model.updated_at.isoformat())

    def test_to_dict_includes_custom_attributes(self):
        """Test that custom attributes are included."""
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89

        obj_dict = model.to_dict()

        self.assertEqual(obj_dict["name"], "My First Model")
        self.assertEqual(obj_dict["my_number"], 89)

    def test_create_from_dictionary(self):
        """Test creating a BaseModel from a dictionary."""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89

        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)

        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.name, model.name)
        self.assertEqual(new_model.my_number, model.my_number)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)

    def test_create_from_dictionary_dates_are_datetime(self):
        """Test dates are converted back to datetime objects."""
        model = BaseModel()
        new_model = BaseModel(**model.to_dict())

        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    def test_create_from_dictionary_ignores_class(self):
        """Test __class__ is not added to the instance."""
        model = BaseModel()
        new_model = BaseModel(**model.to_dict())

        self.assertNotIn("__class__", new_model.__dict__)

    def test_create_from_dictionary_preserves_attributes(self):
        """Test custom attributes are restored."""
        model = BaseModel()
        model.name = "My_First_Model"
        model.my_number = 89

        new_model = BaseModel(**model.to_dict())

        self.assertEqual(new_model.name, "My_First_Model")
        self.assertEqual(new_model.my_number, 89)


if __name__ == "__main__":
    unittest.main()
