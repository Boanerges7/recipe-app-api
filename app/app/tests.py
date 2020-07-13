from app.calc import add, subtract

from django.test import TestCase


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(2, 5), 7)

    def test_substract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(7, 2), 5)
