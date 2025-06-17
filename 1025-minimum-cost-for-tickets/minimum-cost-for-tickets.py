class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days_set = set(days)
        last_day = days[-1]
        dp=[0]*(last_day+1)
        dp[0] = 0
        for i in range(1, last_day+1):
            if i not in days_set:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1]+costs[0], dp[max(0, i-7)]+costs[1], dp[max(0,i-30)]+costs[2])
        return dp[last_day]