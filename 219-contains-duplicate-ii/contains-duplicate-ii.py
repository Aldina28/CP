class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        index = 0
        
        for val in nums:
            if val in seen and index - seen[val] <= k:
                return True
            else:
                seen[val] = index
            index += 1
        
        return False


