class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), w in zip(equations, values):
            graph[a].append([b, w])
            graph[b].append([a, 1/w])

        def dfs(src, dest, result, seen):
            if src in seen:
                return -1
            if src==dest:
                return result
            seen.add(src)
            for neighbours, w in graph[src]:
                temp = dfs(neighbours, dest, result*w, seen)
                if temp != -1:
                    return temp
            return -1
        result = []
        for x, y in queries:
            if x not in graph or y not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(x, y, 1.0, set()))
        return result        

                 