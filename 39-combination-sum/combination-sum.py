class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(i):
            if sum(temp)==target:
                res.append(temp.copy())
                return 
            if i>=len(candidates) or sum(temp)>target:
                return 
            temp.append(candidates[i])
            backtrack(i)
            temp.pop()
            backtrack(i+1)
        backtrack(0)
        return res