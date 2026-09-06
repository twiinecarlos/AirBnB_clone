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
        """Test Place attributes."""
        place = Place()

        place.city_id = "city123"
        place.user_id = "user123"
        place.name = "My Place"
        place.description = "A nice place"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 5
        place.price_by_night = 100
        place.latitude = 1.95
        place.longitude = 30.06
        place.amenity_ids = ["amenity1"]

        self.assertEqual(place.city_id, "city123")
        self.assertEqual(place.user_id, "user123")
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 5)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 1.95)
        self.assertEqual(place.longitude, 30.06)
        self.assertEqual(place.amenity_ids, ["amenity1"])


if __name__ == "__main__":
    unittest.main()
