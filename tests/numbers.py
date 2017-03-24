from __future__ import absolute_import

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
        self.assertEquals(9227465, actual)

    def test_fibonacci_two(self):
        actual = self.fixture.fib2(35)
        self.assertEquals(9227465, actual)

    def test_fibonacci_two_simple(self):
        actual = self.fixture.fib2(2)
        self.assertEquals(1, actual)

    def test_fibonacci_three(self):
        actual = self.fixture.fib3(35)
        self.assertEquals(9227465, actual)

    def test_bullsAndCows(self):
        actual = self.fixture.bullsAndCows("12345", "18275")
        self.assertEquals("2A1B", actual)
