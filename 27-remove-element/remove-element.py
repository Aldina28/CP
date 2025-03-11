class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i=0
        # while i<len(nums):
        #     if nums[i] == val:
        #         nums.remove(nums[i])
        #     else:
        #         i+=1
        # return len(nums)
        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
        return j 