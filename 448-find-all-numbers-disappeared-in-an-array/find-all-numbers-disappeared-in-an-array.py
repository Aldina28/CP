class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        right_array_set = set(range(1,len(nums)+1))
        res = list(right_array_set - set(nums))
        return res
