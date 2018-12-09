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

    def test_msTodhms(self):
        d, h, m, s = self.fixture.msTodhms(362461000)
        self.assertEqual(4, d)
        self.assertEqual(4, h)
        self.assertEqual(41, m)
        self.assertEqual(1, s)

    def test_combination_sum(self):
        self.assertEquals([], self.fixture.combination_sum([], 5))
        self.assertEquals([5], self.fixture.combination_sum([5], 5))
        self.assertEquals([[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [1, 4]], self.fixture.combination_sum([1,2,4], 5))

    def test_countCoin(self):
        array=[2,5,6,3]
        m=len(array)
        n=10
        self.assertEquals(5, self.fixture.countCoin1d(array, m, n))
        self.assertEquals(5, self.fixture.countCoin2d(array, m, n))

    def test_gcd(self):
        self.assertEqual(5, self.fixture.gcd(105,8320))

    def test_count_ways(self):
        self.assertEqual(274, self.fixture.count_ways(10))

    def test_second_largest(self):
        input=[1,3,4,5,0,2]
        self.assertEqual(4, self.fixture.second_largest(input))
        input=[-2, -1]
        self.assertEqual(-2, self.fixture.second_largest(input))
        input=[2,2,1]
        self.assertEqual(2, self.fixture.second_largest(input))

    def test_subsets_of_set(self):
        expected= {'[]', '[3]', '[2]', '[3, 2]', '[1]', '[3, 1]', '[2, 1]', '[3, 2, 1]'}
        actual = self.fixture.subsets_of_set([1,2,3], 0)
        for i in actual:
            actual_str=str(i)
            self.assertTrue(actual_str in expected)

    def test_compute_moving_average(self):
        self.assertEqual(0, self.fixture.computeMovingAverage(None, 0))

        input=[1]
        self.assertEqual(1, self.fixture.computeMovingAverage(input, len(input)))

        input = [1,2,3,4,5,6]
        actual = self.fixture.computeMovingAverage(input, 3)
        self.assertEqual(len(input), len(actual))
        self.assertEqual([1, 1, 2, 3, 4, 5], actual)
        self.assertEqual(-1, self.fixture.computeMovingAverage(input, 10))