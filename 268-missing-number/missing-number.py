class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        result = [0]*(n+1)
        for i in range(len(result)-1):
            result[i+1] = result[i]+1
        print(result)
        for num in result:
            if num not in nums:
                return num 

