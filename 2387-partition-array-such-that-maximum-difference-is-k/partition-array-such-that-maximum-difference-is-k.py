class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums))) 
        ans = 1
        i = nums[0]
        for num in nums[1:]:
            if num - i > k:
                ans += 1
                i = num
        return ans
