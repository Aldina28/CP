class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i=0
        # result = ''
        # while i< max(len(word1), len(word2)):
        #     if i<len(word1):
        #         result+=word1[i]
        #     if i<len(word2):
        #         result+=word2[i]
        #     i+=1
        # return result
        i=0
        j=0
        output = ""

        while i<len(word1) and j<len(word2):
            output+=word1[i]
            output+=word2[j]
            i+=1
            j+=1
        if len(word1)<len(word2):
            output+=word2[j:]
        else:
            output+=word1[i:]
        return output