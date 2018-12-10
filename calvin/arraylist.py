from calvin.point import Point
from calvin.data_structure.queue import Queue

class ArrayList(object):
    def rotate_matrix(self, image):
        if image is None or len(image) == 0 or len(image) != len(image[0]):
            return None

        n = len(image)
        for layer in range(int(n/2)):
            first=layer
            last=n-1-layer
            for i in range(first,last):
                offset=i-first
                top=image[first][i]

                image[first][i] = image[last-offset][first]
                image[last-offset][first] = image[last][last-offset]
                image[last][last-offset] = image[i][last]
                image[i][last] = top

        return image

    def count_island(self, matrix):
        if matrix is None:
            return None

        n = len(matrix)
        m = len(matrix[0])
        number_of_island = 0
        for row in range(n):
            for col in range(m):
                if matrix[row][col]=='X':
                    number_of_island += 1
                    self.__visit_islands(row, col, matrix)

        return number_of_island

    def __visit_islands(self, row, col, matrix):
        if row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) and \
                matrix[row][col]=='X':
            matrix[row][col] = 'm'
            self.__visit_islands(row + 1, col, matrix)
            self.__visit_islands(row - 1, col, matrix)
            self.__visit_islands(row, col + 1, matrix)
            self.__visit_islands(row, col - 1, matrix)

    def only_unconnected_islands(self, matrix):
      if matrix is None:
        return 0

      num_unconnected_islands=0
      n = len(matrix)
      m = len(matrix[0])
      for i in range(n):
        for j in range(m):
          if matrix[i][j]=='X' and not self.__connected(i, j, matrix):
            num_unconnected_islands+=1
      return num_unconnected_islands

    def __connected(self, row, col, matrix):
      connected=False
      # check down
      if row+1 < len(matrix) and not connected:
        connected=matrix[row+1][col]=='X'
      # check up
      if row-1 > 0 and not connected:
          connected=matrix[row-1][col]=='X'
      # check left
      if col-1 > 0 and not connected:
          connected=matrix[row][col-1]=='X'
      # check right
      if col+1 < len(matrix[0]) and not connected:
          connected=matrix[row][col+1]=='X'
      return connected

    def second_largest(self, a):
        if a is None or len(a) < 2:
            return None
        max = -9999999
        for element in a:
            if element > max:
                max = element
        min = 9999999
        result = None
        maxChecked = False
        for element in a:
            if max==element:
                if maxChecked:
                    return element
                maxChecked=True
            elif abs(max - element) < min:
                min = abs(max - element)
                result = element
        return result

    def second_largest_simpler(self, a):
        if a is None:
            return a

        largest = None
        second_largest = None
        for item in a:
            if largest is None:
                largest = item
            elif item > largest:
                second_largest = largest
                largest = item
            elif second_largest is None:
                second_largest = item

        return second_largest

    def get_path(self, maze):
        if maze is None or len(maze) < 1:
            return None
        path=[]
        if self.__get_path(maze, len(maze)-1, len(maze[0])-1, path):
            return path
        return None

    def __get_path(self, maze, row, col, path):
        if col<0 or row<0 or not maze[row][col]:
            return False

        is_at_origin = row==0 and col==0
        if is_at_origin or self.__get_path(maze, row, col-1, path) or self.__get_path(maze, row-1, col, path):
            p=Point(row,col)
            path.append(p)
            return True

        return False

    def shortest_route_to_destination(self, grid):
        if grid is None:
            return None

        source = Point(0,0,0)
        n=len(grid)
        m=len(grid[0])
        visited=[]
        for i in range(n):
            visited.append([False] * m)

        for i in range(n):
            for j in range(m):
                visited[i][j]=grid[i][j]=='X'
                if grid[i][j]=='s':
                    source.row=i
                    source.col=j
                    visited[i][j] = True

        q=Queue()
        q.enqueue(source)
        while not q.isEmpty():
            item=q.dequeue()

            if grid[item.row][item.col]=='e':
                return item.dist

            #move left
            if item.col-1 >= 0 and not visited[item.row][item.col-1]:
                visited[item.row][item.col-1] = True
                q.enqueue(Point(item.row, item.col-1, item.dist+1))

            #move up
            if item.row-1 >= 0 and not visited[item.row-1][item.col]:
                visited[item.row-1][item.col] = True
                q.enqueue(Point(item.row-1, item.col, item.dist+1))

            #move right
            if item.col+1 < m and not visited[item.row][item.col+1]:
                visited[item.row][item.col+1] = True
                q.enqueue(Point(item.row, item.col+1, item.dist+1))

            #move down
            if item.row+1 < n and not visited[item.row+1][item.col]:
                visited[item.row+1][item.col] = True
                q.enqueue(Point(item.row+1, item.col, item.dist+1))

        return None # Not found