class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        for i in range(len(citations)):
            if len(citations) - i <= citations[i]:
                return len(citations)-i
        return 0 
        