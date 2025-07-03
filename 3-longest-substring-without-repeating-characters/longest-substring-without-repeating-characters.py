
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        l = r = 0
        max_length = 0
        while r<len(s):
            if s[r] not in result:
                result.add(s[r])
                max_length = max(max_length, r-l+1)
                r+=1
            else:
                result.remove(s[l])
                l+=1
        return max_length