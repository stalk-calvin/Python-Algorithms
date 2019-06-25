class SudokuBacktracking(object):
    def __init__(self, grid):
        self.grid=grid
        self.grid_size=9
        if not self.grid or len(self.grid)!=self.grid_size or len(self.grid[0])!=self.grid_size:
            raise ('Must initialize the 9x9 board!')

    def print_grid(self):
        print('\n'.join(str(i) for i in self.grid))

    def find_empty_location(self, l):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col]==0:
                    l[0]=row
                    l[1]=col
                    return True
        return False

    def used_in_row(self, row, num):
        for i in range(self.grid_size):
            if self.grid[row][i]==num:
                return True
        return False

    def used_in_col(self, col, num):
        for i in range(self.grid_size):
            if self.grid[i][col]==num:
                return True
        return False

    def used_in_box(self, row_offset, col_offset, num):
        for i in range(3):
            for j in range(3):
                if self.grid[i+row_offset][j+col_offset]==num:
                    return True
        return False

    def is_location_safe(self, row, col, num):
        return not self.used_in_row(row,num) and not self.used_in_col(col,num) and not self.used_in_box(row-row%3,col-col%3,num)

    def solve_sudoku(self):
        l=[0,0]
        if not self.find_empty_location(l):
            # no empty spot
            return True
        row=l[0]
        col=l[1]

        #from 1 to 9
        for num in range(1,10):
            if self.is_location_safe(row,col,num):
                self.grid[row][col]=num
                if self.solve_sudoku():
                    return True
                self.grid[row][col]=0 # didn't make it. reset

        return False