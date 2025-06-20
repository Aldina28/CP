class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        distances = []
        for move in s:
            if move == 'N':
                y+=1
            elif move == 'S':
                y-=1
            elif move == 'E':
                x+=1
            elif move == 'W':
                x-=1
            distances.append(abs(x)+abs(y))
        if k==0:
            return max(distances)
        max_distance = distances[1]
        prev = distances[0]
        added = 0
        for i in range(1, len(distances)):
            if distances[i]<prev and k>0:
                added+=2
                k-=1
            prev = distances[i]
            distances[i] += added
            max_distance = max(max_distance, distances[i])
        return max_distance
            