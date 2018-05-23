import unittest

from calvin.numbers import Numbers

class NumbersTest(unittest.TestCase):
    """
    Test Numbers method
    """
    def setUp(self):
        self.fixture = Numbers()

    def test_fibonacci(self):
        actual = self.fixture.fib(35)
        self.assertEqual(9227465, actual)

    def test_fibonacci_two(self):
        actual = self.fixture.fib2(35)
        self.assertEqual(9227465, actual)

    def test_fibonacci_two_simple(self):
        actual = self.fixture.fib2(2)
        self.assertEqual(1, actual)

    def test_fibonacci_three(self):
        actual = self.fixture.fib3(35)
        self.assertEqual(9227465, actual)

    def test_bullsAndCows(self):
        actual = self.fixture.bullsAndCows("12345", "18275")
        self.assertEqual("2A1B", actual)

    def test_toBinaryNumber(self):
        actual = self.fixture.toBinaryNumber("11000", "01000")
        self.assertEqual("01000", actual)

    def test_sortNumbersBetweenSigns(self):
        actual = self.fixture.sortNumbersBetweenSigns('2+3+1', '+')
        self.assertEqual("1+2+3", actual)

    def test_sortNumbersBetweenSignsWithDifferentSign(self):
        actual = self.fixture.sortNumbersBetweenSigns('2*3*1', '*')
        self.assertEqual("1*2*3", actual)

