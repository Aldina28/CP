class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        i, j = 0, 0
        prev, cur = 0, 0
        for _ in range((m + n) // 2 + 1):
            prev = cur
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    cur = nums1[i]
                    i += 1
                else:
                    cur = nums2[j]
                    j += 1
            elif i < m:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
        
        if (m + n) % 2 == 0:
            return (prev + cur) / 2.0
        else:
            return cur