class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2::]
        count = 0
        print(binary)
        for i in str(binary):
            if i=="1":
                count+=1
        return count