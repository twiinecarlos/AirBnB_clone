#!/usr/bin/python3
"""Unit tests for the Amenity class."""

import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity."""

    def test_create_amenity(self):
        """Test creating an Amenity instance."""
        amenity = Amenity()

        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity.id, str)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)

    def test_amenity_name(self):
        """Test the Amenity name attribute."""
        amenity = Amenity()
        amenity.name = "Wi-Fi"

        self.assertEqual(amenity.name, "Wi-Fi")


if __name__ == "__main__":
    unittest.main()
