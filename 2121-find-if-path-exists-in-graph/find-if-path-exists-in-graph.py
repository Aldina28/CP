class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if [source, destination] in edges or [destination, source] in edges:
            return True
        roots = list(range(n))

        def find(u):
            if u == roots[u]:
                return u
            roots[u] = find(roots[u])
            return roots[u]
        
        for u, v in edges:
            roots[find(u)] = find(v)
        return find(source) == find(destination)
        