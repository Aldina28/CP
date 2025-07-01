class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '')
        res = ""
        for i in s:
            if i.isalpha() or i.isnumeric():
               res+=(i.lower()) 
        return res==res[::-1]