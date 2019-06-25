class WordSearch(object):
    def exist(self, board: [], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if WordSearch.__search_adjacent(board, word[1:], i, j):
                        return True

        return False

    def __search_adjacent(board, word, i, j):
        if word == '':
            return True

        tmp = board[i][j]
        board[i][j] = "#"

        # print(board[i][j], word, i, j)
        if i - 1 >= 0 and board[i - 1][j] == word[0]:
            if WordSearch.__search_adjacent(board, word[1:], i - 1, j):
                return True
        # print(board[i][j], word)

        if i + 1 < len(board) and board[i + 1][j] == word[0]:
            if WordSearch.__search_adjacent(board, word[1:], i + 1, j):
                return True
        # print(board[i][j], word)

        if j - 1 >= 0 and board[i][j - 1] == word[0]:
            if WordSearch.__search_adjacent(board, word[1:], i, j - 1):
                return True
        # print(board[i][j], word)

        if j + 1 < len(board[0]) and board[i][j + 1] == word[0]:
            if WordSearch.__search_adjacent(board, word[1:], i, j + 1):
                return True
        # print(board[i][j], word)

        board[i][j] = tmp
        return False