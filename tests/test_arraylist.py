import unittest

from calvin.arraylist import ArrayList

class ArrayListTest(unittest.TestCase):
    """
    Test Arraylists method
    """
    def setUp(self):
        self.fixture = ArrayList()

    def test_swap_min_max(self):
        actual = [7,5,23,2,7,4,2,3,1,5]
        self.fixture.swapMinMax(actual)
        self.assertEquals([7, 5, 1, 2, 7, 4, 2, 3, 23, 5], actual)

    def test_rotate_image(self):
        input=[]
        c=0
        for x in range(4):
            t=[i for i in range(c,4+c)]
            c+=4
            input.append(t)

        #image: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.assertEquals([[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]],self.fixture.rotate_matrix(input))