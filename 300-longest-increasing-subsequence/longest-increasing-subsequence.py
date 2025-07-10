class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res =[1]*(len(nums)+1)
        res[0]=1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j]<nums[i]:
                    res[i] = max(res[i], res[j]+1)
        return max(res)

            