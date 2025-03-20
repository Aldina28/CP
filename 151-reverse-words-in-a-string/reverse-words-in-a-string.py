class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.split(" ")
        # i=0
        # while i<len(s):
        #     if s[i]=="":
        #         s.remove(s[i])
        #         i-=1
        #     else:
        #         i+=1
        # j = len(s)-2
        # output = [s[len(s)-1]]
        # while j>=0:
        #     output.append(" ")
        #     output.append(s[j])
        #     j-=1
        # output = "".join(output)
        # return output

        # words = s.split()
        # result = []
        # for i in range(len(words)-1, -1, -1):
        #     result.append(words[i])
        #     if i!=0:
        #         result.append(" ")
        # return "".join(result)
        return " ".join(reversed(s.split()))
            
    
        
