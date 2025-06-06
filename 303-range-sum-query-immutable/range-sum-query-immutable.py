class NumArray:

    def __init__(self, nums: List[int]):
        self.result = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.result[i+1] = self.result[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.result[right+1] - self.result[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)