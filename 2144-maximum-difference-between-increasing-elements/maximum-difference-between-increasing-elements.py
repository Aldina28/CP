class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum_diff = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i]<nums[j]:
                    maximum_diff = max(maximum_diff, nums[j]-nums[i])
        return maximum_diff if maximum_diff!=float('-inf') else -1