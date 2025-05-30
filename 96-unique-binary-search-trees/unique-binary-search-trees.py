class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for nodes in range(1, n+1):
            for roots in range(nodes):
                dp[nodes] += dp[roots]*dp[nodes-1-roots]
        return dp[n]