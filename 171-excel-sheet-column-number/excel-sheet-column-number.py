class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in columnTitle:
            pos = ord(i) - ord('A')+1
            res = res*26 + pos
        return res


