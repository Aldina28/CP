class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r=k-1
        min_val = float('inf')
        while r<len(nums):
            min_val = min(min_val, nums[r] - nums[l])
            l += 1
            r += 1
        return min_val


