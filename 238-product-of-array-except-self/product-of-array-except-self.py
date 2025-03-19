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
        count_zero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
            else:
                count_zero+=1
        if count_zero > 1:
            for i in range(len(nums)):
                result.append(0)
        elif count_zero == 1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    result.append(0)
                else:
                    result.append(product)
        else:
            for i in range(len(nums)):
                result.append(product//nums[i])   
        return result