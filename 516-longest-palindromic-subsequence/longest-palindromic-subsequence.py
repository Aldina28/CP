class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0 for _ in range(length + 1)] for _ in range(length+1)]
        reverse = s[::-1]
        for i in range(length-1, -1, -1):
            for j in range(length-1, -1, -1):
                if s[i]==reverse[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]