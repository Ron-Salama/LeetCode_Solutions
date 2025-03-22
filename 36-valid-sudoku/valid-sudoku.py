class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    for k in range(9):
                        if k != i and board[i][j] == board[k][j]:
                            return False
                        if k != j and board[i][j] == board[i][k]:
                            return False
                    if not self.validBox(self.whatBox(i, j), board, board[i][j]):
                        return False
        return True

    def whatBox(self, row, col):
        return [row // 3 * 3, col // 3 * 3]

    def validBox(self, box, board, number):
        count = 0
        for p in range(3):
            for q in range(3):
                if board[box[0] + p][box[1] + q] == number:
                    count += 1
        return count == 1
