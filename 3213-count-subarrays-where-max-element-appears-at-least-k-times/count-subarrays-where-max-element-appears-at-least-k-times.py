class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        temp = 0
        l = 0
        maximum_elt = max(nums)
        for right in nums:
            if right==maximum_elt:
                temp+=1
            while temp>=k:
                if nums[l] == maximum_elt:
                    temp-=1
                l+=1
            count+=l
        return count