class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        visited = set()
        visited.add((0, 0))
        heap = [(0, 0, 0)]

        while heap:
            t, x, y = heappop(heap)
            if (x, y) == (n-1, m-1):
                return t
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0,1)]:
                u, v = dx+x, dy+y
                if 0<=u<n and 0<=v<m and (u, v) not in visited:
                    heappush(heap, (max(t, moveTime[u][v])+1, u, v))
                    visited.add((u, v))
        return -1
