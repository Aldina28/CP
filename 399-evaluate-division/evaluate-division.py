class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), w in zip(equations, values):
            graph[u].append([v, w])
            graph[v].append([u, 1/w])
        
        def bfs(start, target):
            if start not in graph or target not in graph:
                return -1
            queue = deque()
            visit = set()
            queue.append([start, 1])
            visit.add(start)
            while queue:
                n, w = queue.popleft()
                if n==target:
                    return w
                for neigh, weight in graph[n]:
                    if neigh not in visit:
                        queue.append([neigh, w*weight])
                        visit.add(neigh)
            return -1
        
        return [bfs(q[0], q[1]) for q in queries]