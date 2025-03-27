class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        r=k
        sums=max_sum=sum(nums[l:r])
        while r<len(nums):
            sums += nums[r] - nums[l]
            max_sum = max(max_sum, sums)
            l+=1
            r+=1
        return max_sum/k
