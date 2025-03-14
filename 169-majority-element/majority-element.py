class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashMap = {}
        # for i in range(len(nums)):
        #     if nums[i] not in hashMap:
        #         hashMap[nums[i]] = nums.count(nums[i])
        
        # max_count = max(hashMap.values())

        # for key, value in hashMap.items():
        #     if value == max_count and max_count>len(nums)/2:
        #         return key

        nums.sort()
        return nums[len(nums)//2]