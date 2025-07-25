class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        count=1
        end = points[0][1]
        for start, finish in points[1:]:
            if start>end:
                count+=1 
                end = finish
        return count

        # pointer = points[0][1]
        # for i in range(1, len(points)):
        #     if points[i][0]>pointer:
        #         count+=1
        #         pointer = points[i][1]
        # return count 