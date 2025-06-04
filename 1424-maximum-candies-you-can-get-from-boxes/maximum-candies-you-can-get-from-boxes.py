class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        count = 0
        queue = deque(initialBoxes)
        visited = set()
        while queue:
            for i in range(len(queue)):
                box = queue.popleft()
                if box in visited:
                    continue
                visited.add(box)
                if status[box]:
                    count+=candies[box]
                    for k in keys[box]:
                        if k in visited and status[k] == 0:
                            status[k] = 1
                            queue.append(k)
                            visited.remove(k)
                        else:
                            status[k] = 1
                    for extra_box in containedBoxes[box]:
                        queue.append(extra_box)
        return count
       