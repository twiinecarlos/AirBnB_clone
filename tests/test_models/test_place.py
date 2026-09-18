#!/usr/bin/python3
"""Unit tests for the Place class."""

import unittest

from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place."""

    def test_create_place(self):
        """Test creating a Place instance."""
        place = Place()

        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_place_attributes(self):
        """Test Place class attributes."""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertEqual(Place.city_id, "")

        self.assertTrue(hasattr(Place, "user_id"))
        self.assertEqual(Place.user_id, "")

        self.assertTrue(hasattr(Place, "name"))
        self.assertEqual(Place.name, "")

        self.assertTrue(hasattr(Place, "description"))
        self.assertEqual(Place.description, "")

        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertEqual(Place.number_rooms, 0)

        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertEqual(Place.number_bathrooms, 0)

        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertEqual(Place.max_guest, 0)

        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertEqual(Place.price_by_night, 0)

        self.assertTrue(hasattr(Place, "latitude"))
        self.assertEqual(Place.latitude, 0.0)

        self.assertTrue(hasattr(Place, "longitude"))
        self.assertEqual(Place.longitude, 0.0)

        self.assertTrue(hasattr(Place, "amenity_ids"))
        self.assertEqual(Place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
