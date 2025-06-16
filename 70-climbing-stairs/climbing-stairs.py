class Solution:
    def climbStairs(self, n: int) -> int:
        result = [0]*(n+1)
        result[n] = 1
        result[n-1] = 1
        for i in range(n-2, -1, -1):
            result[i] = result[i+1]+result[i+2]
        return result[0]