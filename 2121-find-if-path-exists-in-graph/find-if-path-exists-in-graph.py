class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if [source,destination] in edges or [destination,source] in edges: 
            return True

        graph = list(range(n))

        def find(n):
            if graph[n] != n:
                graph[n] = find(graph[n])

            return graph[n]

        for u,v in edges:
            graph[find(u)] = find(v)

        return find(source) == find(destination)
        