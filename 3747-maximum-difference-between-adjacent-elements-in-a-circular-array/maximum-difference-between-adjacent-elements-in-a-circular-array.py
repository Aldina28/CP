class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = abs(nums[0]-nums[1])
        for i in range(1, len(nums)-1):
            max_diff = max(max_diff, abs(nums[i]-nums[i+1]))
        max_diff = max(max_diff, abs(nums[0]-nums[-1]))
        return max_diff