class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        liist=[]
        for i in range(numRows):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=liist[i-1][j-1]+liist[i-1][j]
            liist.append(row)
        return liist
        