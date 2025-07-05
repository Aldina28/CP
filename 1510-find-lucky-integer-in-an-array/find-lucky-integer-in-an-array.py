class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = [-1]
        counter_array = Counter(arr)
        for key, val in counter_array.items():
            if key == val:
                result.append(key)
        return max(result)