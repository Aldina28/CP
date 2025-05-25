class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_set = set()
        col_set = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)
        for r in (row_set):
                matrix[r] = [0 for _ in range(cols)]
        for j in (col_set):
            for i in range(rows):
                matrix[i][j] = 0