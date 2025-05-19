class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums)-1
        while pivot>0 and nums[pivot-1]>=nums[pivot]:
            pivot-=1
            if pivot == 0:
                nums.reverse()
                return 
        i = len(nums)-1
        while i>=pivot and nums[i]<=nums[pivot-1]:
            i-=1
        nums[i], nums[pivot-1] = nums[pivot-1], nums[i]
        nums[pivot:] = reversed(nums[pivot:])