class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def isValid(mid):
            count, i = 0, 0
            while i<len(nums)-1:
                if abs(nums[i]-nums[i+1])<=mid:
                    count+=1
                    i+=2
                else:
                    i+=1
            if count<p:
                return False
            return True

        low, high = 0, nums[-1]-nums[0]
        while low<=high:
            mid = (low+high)//2
            if isValid(mid):
                ans = mid
                high=mid-1
            else:
                low = mid+1
        return ans
            