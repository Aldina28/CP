class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_val = float("inf")
        l = 0
        sums = 0
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                min_val = min(min_val, r-l+1)
                sums -= nums[l]
                l += 1
        return min_val if min_val!=float("inf") else 0