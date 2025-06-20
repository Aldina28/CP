class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        h = (row*col)-1
        while l<=h:
            mid = (l+h)//2
            i = mid//col
            j = mid%col
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                h = mid-1
            else:
                l = mid+1
        return False