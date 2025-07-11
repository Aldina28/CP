class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(temp.copy())
                return 
            if i>=len(candidates) or curr_sum>target:
                return 
            for j in range(i, len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                temp.append(candidates[j])
                backtrack(j+1, curr_sum+candidates[j])
                temp.pop()
        candidates.sort()
        backtrack(0, 0)
        return res