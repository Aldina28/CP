class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        l = 0
        sums = 0
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                length = min(length, r-l+1)
                sums-=nums[l] 
                l+=1       
        return length if length!=float('inf') else 0