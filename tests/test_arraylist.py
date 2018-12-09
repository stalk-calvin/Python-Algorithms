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
        self.assertEqual([7, 5, 1, 2, 7, 4, 2, 3, 23, 5], actual)

    def test_rotate_image(self):
        input=[]
        c=0
        for x in range(4):
            t=[i for i in range(c,4+c)]
            c+=4
            input.append(t)

        #image: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.assertEqual([[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]],self.fixture.rotate_matrix(input))

    def test_count_island(self):
        input=[
            ['X', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'O', 'O'],
            ['O', 'O', 'X', 'X', 'O'],
            ['O', 'O', 'O', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'X']
        ]
        self.assertEqual(3, self.fixture.count_island(input))

    def test_count_unconnected_island(self):
        input=[
            ['X', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'O', 'O'],
            ['O', 'O', 'X', 'X', 'O'],
            ['O', 'O', 'O', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'X']
        ]
        self.assertEqual(2, self.fixture.only_unconnected_islands(input))

    def test_second_largest(self):
        input=[1,3,4,5,0,2]
        self.assertEqual(4, self.fixture.second_largest(input))
        input=[-2, -1]
        self.assertEqual(-2, self.fixture.second_largest(input))
        input=[2,2,1]
        self.assertEqual(2, self.fixture.second_largest(input))

    def test_get_path(self):
        maze=[
            [1,0,1,1,1],
            [1,1,0,0,1],
            [0,1,0,1,1],
            [1,1,1,0,0],
            [0,0,1,1,1]
        ]
        self.assertEqual(None, self.fixture.get_path(None))
        self.assertEqual("[(0, 0, None), (1, 0, None), (1, 1, None), (2, 1, None), (3, 1, None), (3, 2, None), (4, 2, None), (4, 3, None), (4, 4, None)]", str(self.fixture.get_path(maze)))
        maze=[
            [1,0,1,1,1],
            [1,1,0,0,1],
            [0,0,0,1,1],
            [1,1,1,0,0],
            [0,0,1,1,1]
        ]
        self.assertEqual(None, self.fixture.get_path(maze))

    def test_shortest_route_to_destination(self):
        grid=[
            ['s',' ',' ',' ',' '],
            ['X','X','X','X',' '],
            [' ',' ',' ',' ',' '],
            [' ','X','X','X','X'],
            [' ',' ',' ',' ','e']
        ]
        self.assertEqual(16, self.fixture.shortest_route_to_destination(grid))