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
        """Test City attributes."""
        city = City()

        city.state_id = "state123"
        city.name = "Kigali"

        self.assertEqual(city.state_id, "state123")
        self.assertEqual(city.name, "Kigali")


if __name__ == "__main__":
    unittest.main()
