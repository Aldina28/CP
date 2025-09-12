class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_idx = m-1
        n_idx = n-1
        p = m+n-1
        while n_idx>=0:
            if m_idx>=0 and nums1[m_idx]>nums2[n_idx]:
                nums1[p] = nums1[m_idx]
                p-=1
                m_idx-=1
            else:
                nums1[p] = nums2[n_idx]
                p-=1
                n_idx -=1
    