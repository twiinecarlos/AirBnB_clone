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
        """Test Review class attributes."""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertEqual(Review.place_id, "")

        self.assertTrue(hasattr(Review, "user_id"))
        self.assertEqual(Review.user_id, "")

        self.assertTrue(hasattr(Review, "text"))
        self.assertEqual(Review.text, "")


if __name__ == "__main__":
    unittest.main()
