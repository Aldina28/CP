class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in "\"\':;`~ ,.!?:@#$%^&*()-_=+{}[]/][|\\,.<>":s = s.replace(i, '')
        s = s.upper()
        return s == s[::-1]
