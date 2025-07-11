class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def backtracking(i, sub):
            if i>=len(s):
                res.append(''.join(sub))
                return 
            if s[i].isalpha():
                sub.append(s[i].upper())
                backtracking(i+1, sub)
                sub.pop()

                sub.append(s[i].lower())
                backtracking(i+1, sub)
                sub.pop()
                
            else:
                sub.append(s[i])
                backtracking(i+1, sub)
                sub.pop()
        backtracking(0, [])
        return res