class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        start = 0
        sums = 0
        count = 0
        for end in range(len(nums)):
            sums+=nums[end]
            while sums*(end-start+1)>=k:
                sums -= nums[start]
                start +=1
            count+=(end-start+1)
        return count