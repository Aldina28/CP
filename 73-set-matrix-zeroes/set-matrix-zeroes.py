class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_set = set()
        col_set = set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in row_set:
            matrix[i] = [0 for _ in range(cols)]
        
        for j in col_set:
            for i in range(rows):
                matrix[i][j] = 0
        return matrix