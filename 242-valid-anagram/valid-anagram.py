class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        
        # map1={}
        # map2={}
        # for i in range(len(s)):
        #     if s[i] not in map1:
        #         map1[s[i]] = s.count(s[i])
        #     if t[i] not in map2:
        #         map2[t[i]] = t.count(t[i])
        # if map1==map2:
        #     return True
        # else:
        #     return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t