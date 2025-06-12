class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        runningSum = 0
        startSum = 0
        for num in nums:
            runningSum += num
            startSum = min(startSum, runningSum)
        return -startSum+1 if startSum<1 else 1
        