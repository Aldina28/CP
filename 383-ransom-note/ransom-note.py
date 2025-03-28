class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}
        j=0
        for i in range(len(magazine)):
            if magazine[i] not in hashMap:
                hashMap[magazine[i]] = magazine.count(magazine[i])
        while j<len(ransomNote):
            if ransomNote[j] in hashMap:
                hashMap[ransomNote[j]] -= 1
            else:
                return False
            j+=1
        for key, value in hashMap.items():
            if value<0:
                return False
        return True