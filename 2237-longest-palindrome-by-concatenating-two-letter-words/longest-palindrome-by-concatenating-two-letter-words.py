class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        center = False
        for w in list(count.keys()):
            rev = w[::-1]
            if w == rev:
                res += (count[w]//2)*2
                if count[w]%2:
                    center = True
            elif w<rev:
                res+=2*min(count[w], count[rev])
        return (res+(1 if center else 0))*2
    
           
