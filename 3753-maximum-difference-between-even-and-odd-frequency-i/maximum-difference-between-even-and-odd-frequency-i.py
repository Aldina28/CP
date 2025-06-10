class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_val = 0
        min_val = float('inf')
        for i in counts:
            if counts[i]%2 != 0:
                max_val = max(max_val, counts[i])
            else:
                min_val = min(min_val, counts[i])
        return max_val - min_val