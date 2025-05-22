class Solution:
    def convert(self, s: str, numRows: int) -> str:
        idx = 0
        d = 1
        if numRows==1 or numRows>=len(s):
            return s
        rows = ['']*numRows
        for char in s:
            rows[idx]+=(char)
            if idx == numRows-1:
                d=-1
            elif idx == 0:
                d=1
            idx+=d
        return ''.join(rows)