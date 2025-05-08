class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])

        dist = [[float('inf')]*cols for _ in range(rows)]

        dist[0][0] = 0

        h = [(0,0,0,2)]

        moves = [(0,1),(1,0),(-1,0),(0,-1)]

        while h:
            time, r, c, prev = heappop(h)
            for dx, dy in moves:
                xx, yy = r+dx, c+dy

                if (xx<0 or xx>=rows or yy<0 or yy>=cols):
                    continue
                
                movecost = 2
                if prev==2:
                    movecost = 1

                
                new_time = max(moveTime[xx][yy], dist[r][c]) + movecost

                if new_time < dist[xx][yy]:
                    if (xx==rows-1 and yy==cols-1):
                        return new_time
                    dist[xx][yy] = new_time
                    heappush(h,(new_time, xx, yy, movecost))