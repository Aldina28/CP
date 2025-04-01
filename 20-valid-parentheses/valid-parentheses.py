class Solution:
    def isValid(self, s: str) -> bool:
        mapping={
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack = []
        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                if not stack or char != mapping[stack.pop()]:
                    return False
        return True if stack == [] else False
