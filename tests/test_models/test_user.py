#!/usr/bin/python3
"""Unit tests for the User class."""

import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User."""

    def test_create_user(self):
        """Test creating a User instance."""
        user = User()

        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    def test_user_attributes(self):
        """Test User class attributes."""
        self.assertTrue(hasattr(User, "email"))
        self.assertEqual(User.email, "")

        self.assertTrue(hasattr(User, "password"))
        self.assertEqual(User.password, "")

        self.assertTrue(hasattr(User, "first_name"))
        self.assertEqual(User.first_name, "")

        self.assertTrue(hasattr(User, "last_name"))
        self.assertEqual(User.last_name, "")

    def test_user_inherits_base_model(self):
        """Test that User inherits from BaseModel."""
        from models.base_model import BaseModel

        user = User()

        self.assertIsInstance(user, BaseModel)


if __name__ == "__main__":
    unittest.main()
