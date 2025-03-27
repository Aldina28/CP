class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=1
        max_len=0
        while r<len(nums):
            diff = nums[r] - nums[l]
            if diff==1:
                max_len=max(max_len, r-l+1)
            if diff<=1:
                r+=1
            else:
                l+=1
            
        return max_len
