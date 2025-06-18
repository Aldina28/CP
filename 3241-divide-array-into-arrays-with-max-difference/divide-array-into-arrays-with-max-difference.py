class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums), 3):
            if nums[i+2]-nums[i+1]<=k and nums[i+1]-nums[i]<=k and nums[i+2]-nums[i]<=k:
                res.append([nums[i], nums[i+1], nums[i+2]])
            else:
                res = []
        return res if len(res)==len(nums)//3 else []