class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        sorted_num = dict(sorted(num_count.items(), key=lambda item:item[1], reverse = True))
        result = []
        for i in sorted_num.keys():
            result.append(i)
        return result[0:k]
        