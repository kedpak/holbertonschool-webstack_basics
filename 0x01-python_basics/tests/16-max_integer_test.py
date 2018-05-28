#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__("16-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_int(self):
        self.assertEqual(max_integer([2, 4, 4, 10, 6]), 10)

    def test_empty(self):
        self.assertIsNone(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([3.1, 5.0, 1.2]), 5.0)

    def test_string(self):
        self.assertEqual(max_integer("Holberton"), 't')

    def test_bool(self):
        self.assertEqual(max_integer([True, False]), 1)

    def test_negative(self):
        self.assertEqual(max_integer([-4, -10, -3]), -3)

    def test_mixed_float_int(self):
        self.assertEqual(max_integer([2, 5.5]), 5.5)

    
    
if __name__ == '__main__':
    unittest.main()
