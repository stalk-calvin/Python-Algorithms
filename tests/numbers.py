from __future__ import absolute_import

import unittest
import time

from calvin.numbers import Numbers

class StringsTest(unittest.TestCase):
    """
    Test Strings method
    """
    def setUp(self):
        self.fixture = Numbers()

    def test_fibonacci(self):
        actual = self.fixture.fib(35)
        self.assertEquals(9227465, actual)

    def test_fibonacci_two(self):
        actual = self.fixture.fib2(35)
        self.assertEquals(9227465, actual)

    def test_fibonacci_three(self):
        actual = self.fixture.fib3(35)
        self.assertEquals(9227465, actual)