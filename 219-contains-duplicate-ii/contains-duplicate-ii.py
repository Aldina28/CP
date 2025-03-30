class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        map1={}

        for i, val in enumerate(nums):
            if val in map1 and abs(map1[val]-i)<=k:
                return True
            
            map1[val] = i
        return False
        

        