class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r= 0, 0
        min_len = float('inf')
        result = 0
        for r in range(len(nums)):
            result+=nums[r]
            while result>=target:
                min_len = min(min_len, r-l+1)
                result-=nums[l]
                l+=1

                
        return min_len if min_len != float('inf') else 0
                