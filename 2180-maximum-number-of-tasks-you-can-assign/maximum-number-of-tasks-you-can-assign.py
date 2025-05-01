class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        def can_assign(mid):
            queue = deque()
            pill = pills
            length = len(workers)-1
            for i in reversed(tasks[:mid]):
                if queue and queue[0]>=i:
                    queue.popleft()
                elif length>=0 and workers[length]>=i:
                    length-=1
                else:
                    while length>=0 and workers[length]+strength>=i:
                        queue.append(workers[length])
                        length-=1
                    if not queue or pill==0:
                        return False
                    queue.pop()
                    pill-=1
            return True
        low, high = 0, min(len(workers), len(tasks))
        while low<high:
            mid = (low+high+1)//2
            if can_assign(mid):
                low = mid
            else:
                high = mid-1
        return low