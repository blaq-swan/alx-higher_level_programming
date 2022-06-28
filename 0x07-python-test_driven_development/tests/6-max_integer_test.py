#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test the function 6-max_integer.max_integer"""

    def test_all(self):
        """test positive"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative(self):
        """test negative"""
        self.assertEqual(max_integer([-1, -2, -3, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_no_arg(self):
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        self.assertEqual(max_integer([100]), 100)

    def test_characters(self):
        self.assertEqual(max_integer(['D', 'J', 'P', 'N']), 'P')

    def test_strings(self):
        self.assertEqual(max_integer(["Hello", "World"]), "World")

    def test_non_list(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)

    def test_infinity(self):
        self.assertEqual(max_integer([3, 3, 3]), 3)


if __name__ == "__main__":
    unittest.main()
