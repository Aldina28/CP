class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = []
        for i in prices:
            if buy>i:
                buy = i
            profit.append(i-buy)
            buy = i
        return sum(profit)