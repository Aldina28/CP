class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        def findFirst():
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
                if nums[mid] == target:
                    index = mid
            return index

        def findLast():
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
                if nums[mid] == target:
                    index = mid
            return index

        return [findFirst(), findLast()]
            