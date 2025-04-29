class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        temp = 0
        l = 0
        maximum = max(nums)
        for r in range(len(nums)):
            if nums[r] == maximum:
                temp+=1
            while temp>=k:
                count+=len(nums)-r
                if nums[l]==maximum:
                    temp-=1
                l+=1
        return count

