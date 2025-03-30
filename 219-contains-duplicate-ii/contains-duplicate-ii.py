class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # map1={}

        # for i, val in enumerate(nums):
        #     if val in map1 and abs(map1[val]-i)<=k:
        #         return True
            
        #     map1[val] = i
        # return False

        hm = dict()
        for idx, num in enumerate(nums):
            if num in hm and idx - hm[num] <= k:
                return True
            
            hm[num] = idx
        
        return False