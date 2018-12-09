import unittest

from calvin.bit_manipulation import BitManipulation

class ArrayListTest(unittest.TestCase):
    """
    Test Arraylists method
    """
    def setUp(self):
        self.fixture = BitManipulation()

    def test_merge2bits(self):
        n=int('10000000001',2)
        m=int('10011',2)
        i=2
        j=6
        self.assertEqual(int('10001001101',2), self.fixture.merge2bits(n,m,i,j))

    def test_print_binary(self):
        self.assertEqual('.001', self.fixture.print_binary(.125))
        self.assertEqual('.111', self.fixture.print_binary(0.875))

    def test_longest_sequence(self):
        item=2**32-1
        self.assertEqual(32, self.fixture.longest_sequence(item))
        self.assertEqual('11111111111111111111111111111111', bin(item)[2:])


