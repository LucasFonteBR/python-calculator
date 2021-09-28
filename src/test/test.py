import unittest

from src.calc import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(10, subtract(11, 1))

    def test_divide(self):
        self.assertEqual(3, divide(9, 3))

    def test_multiply(self):
        self.assertEqual(8, multiply(2, 4))
