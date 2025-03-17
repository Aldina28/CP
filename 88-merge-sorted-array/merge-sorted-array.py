class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_idx = m-1
        n_idx = n-1
        ptr = m+n-1

        while n_idx>=0:
            if nums2[n_idx]<nums1[m_idx] and m_idx >= 0:
                nums1[ptr] = nums1[m_idx]
                ptr -= 1
                m_idx -=1
            else:
                nums1[ptr] = nums2[n_idx]
                ptr -= 1
                n_idx -= 1
