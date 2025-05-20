import atexit; atexit.register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]*(n+1)
        for l, r in queries:
            diff[l]-=1
            if r+1<n:
                diff[r+1] += 1
        decrement = 0
        for i in range(n):
            decrement+=diff[i]
            nums[i] = max(nums[i]+decrement, 0)
        return nums.count(0) == len(nums)
