import unittest

from calvin.arraylist import ArrayList, SudokuBacktracking

class SudokuBacktrackingTest(unittest.TestCase):
    def setUp(self):
        grid=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]
        self.fixture=SudokuBacktracking(grid)

    def test_solving_sudoku(self):
        self.fixture.print_grid()
        expected_grid=[
            [3, 1, 6, 5, 7, 8, 4, 9, 2],
            [5, 2, 9, 1, 3, 4, 7, 6, 8],
            [4, 8, 7, 6, 2, 9, 5, 3, 1],
            [2, 6, 3, 4, 1, 5, 9, 8, 7],
            [9, 7, 4, 8, 6, 3, 1, 2, 5],
            [8, 5, 1, 7, 9, 2, 6, 4, 3],
            [1, 3, 8, 9, 4, 7, 2, 5, 6],
            [6, 9, 2, 3, 5, 1, 8, 7, 4],
            [7, 4, 5, 2, 8, 6, 3, 1, 9]
        ]
        self.fixture.solve_sudoku()
        for i in range(9):
            for j in range(9):
                self.assertEqual(expected_grid[i][j], self.fixture.grid[i][j])
        self.fixture.print_grid()


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

    def test_room_size(self):
        rows=[
            '***************',
            '*.....*..*....*',
            '*.....*..*....*',
            '*.....****....*',
            '*******..*....*',
            '*.....*..*....*',
            '*.....*..******',
            '*.....*..*....*',
            '*.....*..*....*',
            '*******..*....*',
            '*.....*..*....*',
            '*.....*..*....*',
            '***************',
            '*...........*.*',
            '*...........*.*',
            '***************',
        ]
        self.assertEqual(22, self.fixture.room_size(15,16,rows))

    def test_sum_rows_columns(self):
        input=[
            [1,0,0,0],
            [1,1,0,0],
            [1,1,1,0],
            [1,1,1,1]
        ]
        self.assertEqual(([1,2,3,4],[4,3,2,1]),self.fixture.sum_rows_columns(input))

    def test_diagonal_word(self):
        input=[list("mooa"),list("oano"),list("otio"),list("ioon")]
        self.assertEqual(('main','anti'), self.fixture.diagonal_word(input))
        input=[list("xoo"),list("oxo"),list("oxx")]
        self.assertEqual(('xxx','oxo'), self.fixture.diagonal_word(input))
        input=[list("a")]
        self.assertEqual(('a','a'), self.fixture.diagonal_word(input))
        input=[list("cxyg"),list("xoaf"),list("mmdl"),list("eooe")]
        self.assertEqual(('code','game'), self.fixture.diagonal_word(input))

    def test_flip_matrix_ud(self):
        input=[
            [1,0,0,0],
            [1,1,0,0],
            [1,1,1,0],
            [1,1,1,1]
        ]
        self.fixture.flip_matrix_ud(input)
        expected=[
            [1,1,1,1],
            [1,1,1,0],
            [1,1,0,0],
            [1,0,0,0]
        ]
        self.assertEqual(expected, input)

    def test_flip_matrix_lr(self):
        input=[
            [1,0,0,0],
            [1,1,0,0],
            [1,1,1,0],
            [1,1,1,1]
        ]
        self.fixture.flip_matrix_lr(input)
        expected=[
            [0,0,0,1],
            [0,0,1,1],
            [0,1,1,1],
            [1,1,1,1]
        ]
        self.assertEqual(expected, input)