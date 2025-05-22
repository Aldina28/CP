class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        long = 0
        left = 0
        for k in s:
            while k in char_set:
                char_set.remove(s[left])
                left +=1
            char_set.add(k)
            if len(char_set)>long:
                long = len(char_set)
        return long
