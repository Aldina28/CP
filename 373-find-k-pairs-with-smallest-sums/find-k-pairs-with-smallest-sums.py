class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        pairs, candidates = [], []
        heapq.heappush(candidates, (nums1[0] + nums2[0], 0, 0))
        while k > 0:
            s, i1, i2 = heapq.heappop(candidates)
            pairs.append((nums1[i1], nums2[i2]))
            k -= 1
            if i2 < n2 - 1:
                heapq.heappush(candidates, (nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
            if i2 == 0 and i1 < n1 - 1:
                heapq.heappush(candidates, (nums1[i1 + 1] + nums2[0], i1 + 1, 0))
        return pairs