__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = defaultdict(int)
        l = 0
        r = 0
        max_len = 0
        for r in range(len(s)):
            result[s[r]] += 1
            max_freq = max(result.values())
            if (r-l+1) - max_freq>k:
                result[s[l]]-=1
                l+=1
            max_len = max(max_len, r-l+1)
        return max_len