class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums_negate = [-x for x in nums]
        heapq.heapify(nums_negate)
        first_pop = -heapq.heappop(nums_negate)
        second_pop = -heapq.heappop(nums_negate)
        return (first_pop-1)*(second_pop-1)