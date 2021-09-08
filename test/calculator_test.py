import unittest
from app.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_of_two_numbers(self):
        self.assertEqual(3.7, self.calc.add(1.2, 2.5))

    def test_difference_of_two_numbers(self):
        self.assertAlmostEqual(7.7, self.calc.subtract(10.2, 2.5))
