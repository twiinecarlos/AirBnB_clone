#!/usr/bin/python3
"""Unit tests for the Review class."""

import unittest

from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review."""

    def test_create_review(self):
        """Test creating a Review instance."""
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.id, str)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_review_attributes(self):
        """Test Review attributes."""
        review = Review()

        review.place_id = "place123"
        review.user_id = "user123"
        review.text = "Great place!"

        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user123")
        self.assertEqual(review.text, "Great place!")


if __name__ == "__main__":
    unittest.main()
