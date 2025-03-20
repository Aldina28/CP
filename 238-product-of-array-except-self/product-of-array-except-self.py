class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # product = 1
        # for i in range(len(nums)):
        #     l=i-1
        #     r=i+1

        #     while l>=0 and r<= len(nums)-1:
        #         product *= (nums[l]*nums[r])
        #         l-=1
        #         r+=1
        #     while l>=0:
        #             product*=nums[l] 
        #             l-=1

        #     while r<=len(nums)-1:
        #             product*=nums[r]
        #             r+=1
        #     result.append(product)
        #     product = 1
        # return result

        result = []
        product = 1
        zero_count = nums.count(0)

        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            
        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    result.append(product)
                else:
                    result.append(0)
            
        elif zero_count == 0:
            for i in range(len(nums)):
                result.append((product//nums[i]))
        
        else:
            for i in range(len(nums)):
                result.append(0)
        return result        