#!/usr/bin/python3
"""Unit tests for the State class."""

import unittest

from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State."""

    def test_create_state(self):
        """Test creating a State instance."""
        state = State()

        self.assertIsInstance(state, State)
        self.assertIsInstance(state.id, str)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    def test_state_name(self):
        """Test the State name attribute."""
        state = State()
        state.name = "Kigali"

        self.assertEqual(state.name, "Kigali")


if __name__ == "__main__":
    unittest.main()
