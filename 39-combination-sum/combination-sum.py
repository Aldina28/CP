class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(temp[:])
                return
            if i >= len(candidates) or curr_sum > target:
                return

            temp.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            temp.pop()
            backtrack(i + 1, curr_sum)
        backtrack(0, 0)
        return res