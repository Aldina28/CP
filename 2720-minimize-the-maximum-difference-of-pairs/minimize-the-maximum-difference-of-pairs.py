class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def isValid(mid):
            count, i = 0, 1
            while i<len(nums):
                if (nums[i]-nums[i-1])<=mid:
                    count+=1
                    i+=1
                i+=1
            return count
        low, high = 0, nums[-1]-nums[0]
        while low<=high:
            mid = (low+high)//2
            if isValid(mid) >= p:
                ans = mid
                high=mid-1
            else:
                low = mid+1
        return low