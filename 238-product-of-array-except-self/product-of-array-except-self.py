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

        output = [1]*len(nums)
        l=1
        for i in range(len(nums)):
            output[i] *= l
            l*=nums[i]

        r=1
        for i in range(len(nums)-1, -1, -1):
            output[i]*=r  
            r*=nums[i]
        
        return output