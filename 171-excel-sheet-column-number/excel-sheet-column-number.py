class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n=len(columnTitle)
        for i in columnTitle:
            res = res + (ord(i)-ord("A")+1)*26**(n-1)
            n-=1
        return res
