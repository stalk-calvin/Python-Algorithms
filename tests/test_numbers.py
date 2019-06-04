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

    def test_binarySearchIterative(self):
        input=[2,5,7,9,12,18,25]
        self.assertEqual(12, self.fixture.binarySearchIterative(input, 12))
        input=[12]
        self.assertEqual(12, self.fixture.binarySearchIterative(input, 12))
        input=[]
        self.assertEqual(-1, self.fixture.binarySearchIterative(input, 12))
        input=[2, 5, 7, 9, 12, 18, 25]
        self.assertEqual(-1, self.fixture.binarySearchIterative(input, 15))
        input=[13]
        self.assertEqual(-1, self.fixture.binarySearchIterative(input, 15))

    def test_binarySearchRecursive(self):
        input=[2,5,7,9,12,18,25]
        self.assertEqual(12, self.fixture.binarySearchRecursive(input, 12, 0, len(input)-1))
        input=[12]
        self.assertEqual(12, self.fixture.binarySearchRecursive(input, 12, 0, len(input)-1))
        input=[]
        self.assertEqual(-1, self.fixture.binarySearchRecursive(input, 12, 0, len(input)-1))
        input=[2, 5, 7, 9, 12, 18, 25]
        self.assertEqual(-1, self.fixture.binarySearchRecursive(input, 15, 0, len(input)-1))
        input=[13]
        self.assertEqual(-1, self.fixture.binarySearchRecursive(input, 15, 0, len(input)-1))

    def test_swap_min_max(self):
        input = [7,5,23,2,7,4,2,3,1,5]
        self.fixture.swapMinMax(input)
        self.assertEqual([7, 5, 1, 2, 7, 4, 2, 3, 23, 5], input)

    def test_rotated_sorted_array(self):
        input = [3,4,5,6,7,8,9]
        self.assertEqual(4, self.fixture.rotated_search(input, 4))
        self.assertEqual(3, self.fixture.rotated_search(input, 3))
        self.assertEqual(9, self.fixture.rotated_search(input, 9))
        self.assertEqual(8, self.fixture.rotated_search(input, 8))

        input = [3,7,8,9,1,2]
        self.assertEqual(7, self.fixture.rotated_search(input, 7))
        self.assertEqual(8, self.fixture.rotated_search(input, 8))
        self.assertEqual(2, self.fixture.rotated_search(input, 2))
        self.assertRaises(Exception, self.fixture.rotated_search, input, 'abc')
        self.assertRaises(Exception, self.fixture.rotated_search, input, None)
        self.assertEqual(None, self.fixture.rotated_search(None, None))

        input = [2,2,2,3,3,4,4,4,4,5,6,7]
        self.assertEqual(6, self.fixture.rotated_search(input, 6))
        self.assertEqual(7, self.fixture.rotated_search(input, 7))
        self.assertEqual(2, self.fixture.rotated_search(input, 2))
        self.assertEqual(5, self.fixture.rotated_search(input, 5))

        input = [3]
        self.assertEqual(3, self.fixture.rotated_search(input, 3))
        self.assertEqual(-1, self.fixture.rotated_search(input, 4))

    def test_sum_swap(self):
        a=[4, 1, 2, 1, 1, 2]
        b=[3, 6, 3, 3]
        self.assertEqual({(1, 3), (4, 6)},self.fixture.sum_swap(a,b))
        self.assertEqual(None, self.fixture.sum_swap(a, None))
        a=[1, 1, 1, 1, 1, 1]
        b=[5, 5, 5, 5, 5, 5]
        self.assertEqual(set(), self.fixture.sum_swap(a, b))

    def test_sum_swap_target(self):
        # O(ab)
        a=[4, 1, 2, 1, 1, 2]
        b=[3, 6, 3, 3]
        self.assertEqual({(1, 3), (4, 6)},self.fixture.sum_swap_target(a,b))
        self.assertEqual(None, self.fixture.sum_swap(a, None))
        a=[1, 1, 1, 1, 1, 1]
        b=[5, 5, 5, 5, 5, 5]
        self.assertEqual(set(),self.fixture.sum_swap_target(a,b))

    def test_smallest_k(self):
        input=[1,6,2,3,4,7,8,9,10]
        self.assertEqual([1,2,3,4,6], self.fixture.smallest_k(input, 5))
        self.assertEqual([1, 2, 3, 4, 6, 7, 8, 9, 10], self.fixture.smallest_k(input, 15))
        self.assertEqual(None, self.fixture.smallest_k(None, 5))

    def test_is_magic(self):
        input=[1,2,3,4]
        self.assertFalse(self.fixture.is_magic(9, input, 0, 0))
        self.assertFalse(self.fixture.is_magic(3, input, 0, 0))
        self.assertTrue(self.fixture.is_magic(6, input, 0, 0))

    def test_peakram(self, ):
        class logentry(object):
            def __init__(self, start, end, ram):
                self.ram=ram
                self.start=start
                self.end=end

        A=[
            logentry(1, 2, 1),
            logentry(3, 4, 8),
            logentry(2, 4, 3),
            logentry(5, 6, 10)
        ]
        # --- (1 GB)
        #     --- (8 GB)
        #   ----- (3 GB)
        #         --- (10GB)
        # 1 2 3 4 5 6
        self.assertEqual(11, self.fixture.peak_ram(A))

        A=[
            logentry(0,100,500),
            logentry(10,70,300),
            logentry(50,200,1000),
            logentry(110,220,400),
            logentry(175,280,750)
        ]
        self.assertEqual(2150, self.fixture.peak_ram(A))

        A=[
            logentry(0,100,50),
            logentry(50,250,1000),
            logentry(100,125,240),
            logentry(150,175,300)
        ]
        self.assertEqual(1300, self.fixture.peak_ram(A))

    def test_deficinet_number(self):
        self.assertEqual([5, 14, 1596, 231, 1560, 491, 186, 16, 395, 178],
         self.fixture.deficient_number(10,
          [(1,4),(6,10),(34,89),(12,34),(37,90),(12,47),(39,47),(17,18),(78,87),(23,36)]))
        self.assertEqual([1,1,1,1,1],self.fixture.deficient_number(5,[(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)]))
        self.assertEqual([0,0,0,0],self.fixture.deficient_number(4,[(6,6),(12,12),(18,18),(20,20)]))