class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count =  Counter(nums)
        result = []
        sorted_nums = sorted(nums_count.items(), key=lambda item:item[1], reverse=True)
        result = [item[0] for item in sorted_nums[:k]]
        return result
        