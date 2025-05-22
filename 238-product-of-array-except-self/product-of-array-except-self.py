class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        total_product = 1
        result = []
        for i in range(len(nums)):
            if nums[i]!=0:
                total_product *= nums[i]
        if zero_count==0:
            for i in range(len(nums)):
                result.append(total_product//nums[i])
        elif zero_count==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    result.append(0)
                else:
                    result.append(total_product)
        elif zero_count>1:
            for i in range(len(nums)):
                result.append(0)
        return result
                 