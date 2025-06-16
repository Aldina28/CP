class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum = nums[0]
        difference = -1
        for i in nums[1:]:
            if i<=minimum:
                minimum = i
            else:
                difference = max(difference, i-minimum)
        return difference 