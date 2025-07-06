class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left=0
        s1count=Counter(s1)
        
        wincount=Counter()
        for right in range(len(s2)):
            wincount[s2[right]]+=1
            if right-left+1 >len(s1):
                wincount[s2[left]]-=1
                if wincount[s2[left]]==0:
                    del wincount[s2[left]]
                left+=1
            if wincount==s1count:
                return True
        return False