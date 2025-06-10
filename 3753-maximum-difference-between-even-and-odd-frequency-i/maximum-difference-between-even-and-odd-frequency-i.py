class Solution:
    def maxDifference(self, s: str) -> int:
        hashMap = {}
        for i in s:
            if i not in hashMap:
                hashMap[s.count(i)] = i
        odds = list()
        even = list()
        for val in hashMap.keys():
            if val%2 != 0:
                odds.append(val)
            else:
                even.append(val)
        max_odds=max(odds)
        min_even = min(even)
        return max_odds - min_even
        
            
