class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count =  Counter(nums)
        result = []
        sorted_nums = dict(sorted(nums_count.items(), key=lambda items:items[1], reverse = True))
        for i in sorted_nums.keys():
            result.append(i)
        return result[0:k]
        