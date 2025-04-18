class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res=[]
        for i in range(rows):
            for j in range(cols):
                res.append([i, j])
        
        res.sort(key=lambda s:abs(s[0]-rCenter)+abs(s[1]-cCenter))
        return res
