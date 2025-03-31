class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        result = []
        prev = intervals[0]
        for i in intervals[1:]:
            if i[0] <= prev[1]:
                prev[1] = max(prev[1], i[1])
            else:
                result.append(prev)
                prev = i 
        result.append(prev)
        return result
