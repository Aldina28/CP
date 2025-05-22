class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current = result[-1]
            if current[-1]>= intervals[i][0]:
                current[-1] = max(current[-1], intervals[i][-1])
            else:
                result.append(intervals[i])
        return result