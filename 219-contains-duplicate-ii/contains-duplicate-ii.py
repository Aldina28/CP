class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        map1=dict()

        for i, val in enumerate(nums):
            if val in map1 and i-map1[val]<=k:
                return True
            map1[val] = i
        return False
        

        