class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in hashMap:
                if i!=hashMap[target-nums[i]]:
                    return [i, hashMap[target-nums[i]]]

        