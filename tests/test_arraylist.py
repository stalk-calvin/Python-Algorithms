import unittest

from calvin.arraylist import ArrayList

class ArrayListTest(unittest.TestCase):
    """
    Test Arraylists method
    """
    def setUp(self):
        self.fixture = ArrayList()

    # image:
    # [
    #  [0, 1, 2, 3],
    #  [4, 5, 6, 7],
    #  [8, 9, 10, 11],
    #  [12, 13, 14, 15]
    # ]
    def test_rotate_image(self):
        input=[]
        c=0
        for x in range(4):
            t=[i for i in range(c,4+c)]
            c+=4
            input.append(t)

        self.assertEqual([[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]],self.fixture.rotate_matrix(input))

    # image:
    # [
    #  [0, 1, 2, 3],
    #  [4, 5, 6, 7],
    #  [8, 9, 10, 11],
    #  [12, 13, 14, 15]
    # ]
    def test_rotate_right_simpler(self):
        input=[]
        c=0
        for x in range(4):
            t=[i for i in range(c,4+c)]
            c+=4
            input.append(t)

        self.assertEqual([[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]],
                         self.fixture.rotate_right_90_degrees_simpler(input))

    # image:
    # [
    #  [0, 1, 2, 3],
    #  [4, 5, 6, 7],
    #  [8, 9, 10, 11],
    #  [12, 13, 14, 15]
    # ]
    def test_rotate_left_simpler(self):
        input=[]
        c=0
        for x in range(4):
            t=[i for i in range(c,4+c)]
            c+=4
            input.append(t)

        self.assertEqual([[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]],
                         self.fixture.rotate_left_90_degrees_simpler(input))

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
        input = [1, 2, 3]
        self.assertEqual(2, self.fixture.second_largest(input))
        self.assertEqual(None, self.fixture.second_largest(None))

    def test_second_largest_simpler(self):
        input=[1,3,4,5,0,2]
        self.assertEqual(4, self.fixture.second_largest_simpler(input))
        input=[-2, -1]
        self.assertEqual(-2, self.fixture.second_largest_simpler(input))
        input=[2,2,1]
        self.assertEqual(2, self.fixture.second_largest_simpler(input))

    def test_get_path(self):
        maze=[
            [1,0,1,1,1],
            [1,1,0,0,1],
            [0,1,0,1,1],
            [1,1,1,0,0],
            [0,0,1,1,1]
        ]
        expected=[
            (0, 0, None),
            (1, 0, None),
            (1, 1, None),
            (2, 1, None),
            (3, 1, None),
            (3, 2, None),
            (4, 2, None),
            (4, 3, None),
            (4, 4, None)]
        self.assertEqual(str(expected), str(self.fixture.get_path(maze)))
        maze=[
            [1,0,1,1,1],
            [1,1,0,0,1],
            [0,0,0,1,1],
            [1,1,1,0,0],
            [0,0,1,1,1]
        ]
        self.assertEqual(None, self.fixture.get_path(maze))
        self.assertEqual(None, self.fixture.get_path(None))

    def test_shortest_route_to_destination(self):
        grid=[
            ['s',' ',' ',' ',' '],
            ['X','X','X','X',' '],
            [' ',' ',' ',' ',' '],
            [' ','X','X','X','X'],
            [' ',' ',' ',' ','e']
        ]
        self.assertEqual(16, self.fixture.shortest_route_to_destination(grid))