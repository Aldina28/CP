class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)
        self.keys = sorted(self.freq1.keys())
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index]+=val
        self.freq2[self.nums2[index]] +=1

    def count(self, tot: int) -> int:
        count = 0
        for i in self.keys:
            if i>=tot:
                break
            if tot-i in self.freq2:
                count+=self.freq1[i] * self.freq2[tot-i]
        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)