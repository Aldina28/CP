class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        max_len = 0
        l, r = 0, 0
        while r<len(s):
            if s[r] not in result:
                result.add(s[r])
                max_len = max(max_len, r-l+1)
                r+=1
            elif s[r] in result:
                result.remove(s[l])
                l+=1
        return max_len
