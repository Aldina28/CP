class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def sub(i, s1):
            if i>=len(s):
                res.append(s1)
                return 
            if s[i].isalpha():
                sub(i+1, s1+s[i].lower())
                sub(i+1, s1+s[i].upper())
            else:
                sub(i+1, s1+s[i])
        s1 = ''
        sub(0, s1)
        return res