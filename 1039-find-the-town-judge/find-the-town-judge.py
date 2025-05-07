class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        people = [0] * n
        pos = []
        for (l,r) in trust:
            if people[r-1] >= 0:
                people[r-1] += 1
                if people[r-1] == n-1:
                    pos.append(r-1)
            people[l-1] = -1 
        
        for p in pos:
            if people[p] == n-1:
                return p +1
        return -1