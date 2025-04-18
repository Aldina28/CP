class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[i,j] for i in range(rows) for j in range(cols)], key=lambda s:abs(s[0]-rCenter)+abs(s[1]-cCenter))
