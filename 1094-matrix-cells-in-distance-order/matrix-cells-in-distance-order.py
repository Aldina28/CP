class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def distance(pos):
            i, j = pos
            return abs(i - rCenter) + abs(j - cCenter)

        res = [(i, j) for i in range(rows) for j in range(cols)]
        return sorted(res, key=distance)
