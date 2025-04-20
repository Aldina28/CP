class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = list(s)
        n = len(a)
        l, r = 0, n -1
        while l < r: 
            while l < r and a[l] not in vowels: 
                l += 1
            while l < r and a[r] not in vowels: 
                r -= 1 
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
        return ''.join(a)