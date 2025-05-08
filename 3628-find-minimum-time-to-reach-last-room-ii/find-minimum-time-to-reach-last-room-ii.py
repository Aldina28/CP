class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        if n==1 or m==1:
            return 0
        visited = set()
        visited.add((0, 0))
        h=[(0, 0, 0, 0)]
        while h:
            t, x, y, step = heappop(h)
            if (x, y) == (n-1, m-1):
                return t
            if (x, y, step % 2) in visited:
                continue
            visited.add((x, y, step % 2))
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                u, v = dx+x, dy+y
                if 0<=u<n and 0<=v<m:
                    move_cost = 1 if step % 2 == 0 else 2
                    depart_time = max(t, moveTime[u][v])
                    arrival_time = depart_time + move_cost
                    heappush(h, (arrival_time, u, v, step + 1))
        return -1