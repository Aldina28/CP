class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        n=len(nums1)
        if(n%2==0):
            x=nums1[n//2-1]+nums1[n//2]
            return x/2
        else:
            return nums1[n//2]