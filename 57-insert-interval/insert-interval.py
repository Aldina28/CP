class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for i in range(1,len(intervals)):
            current = result[-1]
            if current[1]>=intervals[i][0]:
                current[1] = max(current[1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result
                
        