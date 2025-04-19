class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = len(nums)-1
        while ptr>0 and nums[ptr-1]>=nums[ptr]:
            ptr -= 1
        if ptr==0:
            nums.reverse()
            return 
        j = len(nums)-1
        while j>=ptr and nums[j]<=nums[ptr-1]:
            j-=1
        nums[ptr-1], nums[j] = nums[j], nums[ptr-1]
        nums[ptr:]=reversed(nums[ptr:])