class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i = 0
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.remove(nums[i+1])
        #     else:
        #         i+=1
        # return len(nums)

        i=0
        j=0
        while i<len(nums) and j<len(nums):
            if nums[i]!=nums[j]:
                nums[i+1] = nums[j]
                i+=1
            j+=1
        return i+1

        