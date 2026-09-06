#!/usr/bin/python3
"""Unit tests for the FileStorage class."""

import json
import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage."""

    def setUp(self):
        """Set up a clean storage for each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Clean up the storage file after each test."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all_returns_dictionary(self):
        """Test that all returns a dictionary."""
        storage_obj = FileStorage()
        self.assertIsInstance(storage_obj.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds an object."""
        storage_obj = FileStorage()
        model = BaseModel()

        storage_obj.new(model)

        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage_obj.all())
        self.assertIs(storage_obj.all()[key], model)

    def test_save_creates_file(self):
        """Test that save creates file.json."""
        storage_obj = FileStorage()
        model = BaseModel()

        storage_obj.new(model)
        storage_obj.save()

        self.assertTrue(os.path.exists("file.json"))

    def test_save_writes_json(self):
        """Test that save writes valid JSON."""
        storage_obj = FileStorage()
        model = BaseModel()
        model.name = "Test"

        storage_obj.new(model)
        storage_obj.save()

        with open("file.json", "r") as file:
            data = json.load(file)

        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, data)
        self.assertEqual(data[key]["name"], "Test")

    def test_reload_restores_object(self):
        """Test that reload restores objects from file."""
        storage_obj = FileStorage()
        model = BaseModel()
        model.name = "Test"

        storage_obj.new(model)
        storage_obj.save()

        FileStorage._FileStorage__objects = {}
        storage_obj.reload()

        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage_obj.all())
        self.assertIsInstance(storage_obj.all()[key], BaseModel)
        self.assertEqual(storage_obj.all()[key].name, "Test")

    def test_reload_restores_id(self):
        """Test that reload restores the original ID."""
        storage_obj = FileStorage()
        model = BaseModel()

        storage_obj.new(model)
        storage_obj.save()

        FileStorage._FileStorage__objects = {}
        storage_obj.reload()

        key = "BaseModel.{}".format(model.id)
        self.assertEqual(storage_obj.all()[key].id, model.id)

    def test_reload_without_file_does_not_raise(self):
        """Test reload when file.json does not exist."""
        storage_obj = FileStorage()

        storage_obj.reload()

        self.assertEqual(storage_obj.all(), {})

    def test_base_model_is_added_to_storage(self):
        """Test that new BaseModel instances enter storage."""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, storage.all())

    def test_base_model_save_calls_storage(self):
        """Test that BaseModel.save persists the object."""
        model = BaseModel()
        model.name = "Saved Model"
        model.save()

        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as file:
            data = json.load(file)

        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, data)
        self.assertEqual(data[key]["name"], "Saved Model")


if __name__ == "__main__":
    unittest.main()
