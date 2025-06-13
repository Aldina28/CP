class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sum, nums1_zeroes = sum(nums1), nums1.count(0)
        nums2_sum, nums2_zeroes = sum(nums2), nums2.count(0)
        if (nums1_zeroes == 0 and nums1_sum<nums2_sum+nums2_zeroes) or (nums2_zeroes==0 and nums2_sum<nums1_sum+nums1_zeroes):
            return -1
        return max(nums1_sum+nums1_zeroes, nums2_sum+nums2_zeroes)
