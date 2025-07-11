class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(i, temp):
            if i>=len(s):
                res.append(temp)
                return 
            
            if s[i].isalpha():
                backtrack(i+1, temp+s[i].upper())
                backtrack(i+1, temp+s[i].lower())
            else:
                backtrack(i+1, temp+s[i])
        temp = ''
        backtrack(0, temp)
        return res