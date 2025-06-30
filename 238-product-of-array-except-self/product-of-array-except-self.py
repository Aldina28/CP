
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        zero_count = nums.count(0)
        product = 1
        if zero_count==0:
            for i in range(len(nums)):
                product*=nums[i]
            for i in range(len(nums)):
                result.append(product//nums[i])
        
        elif zero_count == 1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    product*=nums[i]
            for i in range(len(nums)):
                if nums[i]==0:
                    result.append(product)
                else:
                    result.append(0)

        elif zero_count>1:
            for i in range(len(nums)):
                result.append(0)
        return result