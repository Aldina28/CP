class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        max_val = -float('inf')
        min_val = float('inf')
        for key, val in counts.items():
            if val%2 != 0:
                max_val = max(max_val, val)
            else:
                min_val = min(min_val, val)
        return max_val - min_val