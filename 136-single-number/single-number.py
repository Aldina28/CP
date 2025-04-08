class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hashMap = {}
        # for i in range(len(nums)):
        #     if nums[i] not in hashMap:
        #         hashMap[nums[i]] = nums.count(nums[i])
        # for key, values in hashMap.items():
        #     if values==1:
        #         return key
        HashMap = Counter(nums)

        for item in HashMap:
            if HashMap[item] == 1:
                return item
