class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l, h = 0, len(nums)-1
        result = []
        while l<h:
            min_elt = nums[l]
            max_elt = nums[h]
            avg = (min_elt+max_elt)/2
            if avg not in result:
                result.append(avg) 
            l+=1
            h-=1
        return len(result)          