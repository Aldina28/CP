class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        result_set = set()
        while nums:
            max_elt = nums.pop()
            min_elt = nums.pop(0)
            avg = (max_elt+min_elt)/2
            result_set.add(avg)
        return len(result_set)            