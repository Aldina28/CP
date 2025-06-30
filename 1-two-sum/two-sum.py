class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashMap:
                return [i, hashMap[difference]]
            hashMap[nums[i]]=i
        