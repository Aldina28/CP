class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # seen = {}
        # index = 0
        
        # for val in nums:
        #     if val in seen and index - seen[val] <= k:
        #         return True
        #     else:
        #         seen[val] = index
        #     index += 1
        
        # return False
        map1={}

        for i, val in enumerate(nums):
            if val in map1 and abs(map1[val]-i)<=k:
                return True
            
            map1[val] = i
        return False