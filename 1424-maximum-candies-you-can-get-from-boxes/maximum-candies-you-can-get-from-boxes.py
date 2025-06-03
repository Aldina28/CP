class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque(initialBoxes)
        n = len(status)
        visited = [False] * n
        hasBox = [False] * n
        hasKey = status[:]
        count = 0

        for box in initialBoxes:
            hasBox[box] = True

        while queue:
            box = queue.popleft()
            if visited[box] or not hasKey[box]:
                continue

            visited[box] = True
            count += candies[box]

            for b in containedBoxes[box]:
                hasBox[b] = True
                queue.append(b)

            for k in keys[box]:
                hasKey[k] = 1
                if hasBox[k]:
                    queue.append(k)

        return count