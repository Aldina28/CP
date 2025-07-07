class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        n1= len(s1)
        n2 = len(s2)

        array1 = [0]*26
        array2 = [0]*26

        for i in range(n1):
            array1[ord(s1[i])-97]  +=1
            array2[ord(s2[i])-97] +=1
        
        if array1 == array2:
            return True
        
        for i in range(n1, n2):
            array2[ord(s2[i])-97] +=1
            array2[ord(s2[i-n1])-ord('a')]-=1
            if array1==array2:
                return True
        return False