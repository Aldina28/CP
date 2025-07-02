class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            '(':')', 
            '{':'}',
            '[':']'
        }
        stack = []
        for i in s:
            if i in hashMap.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                popelt = stack.pop()
                if popelt in hashMap.keys() and hashMap[popelt] != i:
                    return False
        return stack == []