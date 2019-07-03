class One_8(object):
    def zero_matrix(self, matrix):
        def null_rows(matrix, row):
            for i in range(len(matrix[0])):
                matrix[row][i] = 'x'

        def null_cols(matrix, col):
            for i in range(len(matrix)):
                matrix[i][col] = 'x'

        row = [False]*len(matrix)
        col = [False]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    null_rows(matrix, i)
                    null_cols(matrix, j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
