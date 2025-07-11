class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hashMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []
        def backtrack(i, temp):
            if i>=len(digits):
                res.append(temp)
                return 
            for letter in hashMap[digits[i]]:
                backtrack(i + 1, temp + letter)
        backtrack(0, '')
        return res