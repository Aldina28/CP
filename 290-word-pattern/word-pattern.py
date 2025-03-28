class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = {}
        map2 = {}
        s=list(s.split(" "))
        if len(pattern)!=len(s):
            return False
        for i in range(len(s)):
            if pattern[i] not in map1:
                map1[pattern[i]] = i
            if s[i] not in map2:
                map2[s[i]] = i
            if map1[pattern[i]] != map2[s[i]]:
                return False
        return True