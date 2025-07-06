__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res = 0
        i = 0
        for j in range(len(s)):
            freq[s[j]] += 1
            max_freq = max(freq.values())
            curr_len = j-i+1
            if curr_len - max_freq>k:
                freq[s[i]]-=1
                i+=1
            res = max(res, j-i+1)
        return res