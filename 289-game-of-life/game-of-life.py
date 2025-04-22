class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_num = len(board)
        col_num = len(board[0])
        zero_count = []
        original = [row[:] for row in board]
        for r in range(row_num):
            for c in range(col_num):
                if r - 1 >= 0:
                    zero_count.append(original[r - 1][c])
                if r + 1 < row_num:
                    zero_count.append(original[r + 1][c])
                if c - 1 >= 0:
                    zero_count.append(original[r][c - 1])
                if c + 1 < col_num:
                    zero_count.append(original[r][c + 1])
                if r - 1 >= 0 and c - 1 >= 0:
                    zero_count.append(original[r - 1][c - 1])
                if r - 1 >= 0 and c + 1 < col_num:
                    zero_count.append(original[r - 1][c + 1])
                if r + 1 < row_num and c + 1 < col_num:
                    zero_count.append(original[r + 1][c + 1])
                if r + 1 < row_num and c - 1 >= 0:
                    zero_count.append(original[r + 1][c - 1])
                ones = zero_count.count(1)

                if original[r][c] == 0:
                    if ones == 3:
                        board[r][c] = 1
                else:
                    if ones < 2 or ones > 3:
                        board[r][c] = 0
                    else:
                        board[r][c] = 1
                zero_count=[]
