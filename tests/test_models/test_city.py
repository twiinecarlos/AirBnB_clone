#!/usr/bin/python3
"""Unit tests for the City class."""

import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City."""

    def test_create_city(self):
        """Test creating a City instance."""
        city = City()

        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_city_attributes(self):
        """Test City class attributes."""
        self.assertTrue(hasattr(City, "state_id"))
        self.assertEqual(City.state_id, "")

        self.assertTrue(hasattr(City, "name"))
        self.assertEqual(City.name, "")


if __name__ == "__main__":
    unittest.main()
