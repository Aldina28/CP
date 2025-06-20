class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque([startGene])
        visited = set([startGene])
        mutations = 0
        while queue:
            for _ in range(len(queue)): 
                gene = queue.popleft()
                if gene == endGene:
                    return mutations
                for c in 'AGCT':
                    for i in range(len(gene)):
                        neighbor = gene[:i]+c+gene[i+1:]
                        if neighbor not in visited and neighbor in bank:
                            queue.append(neighbor)
                            visited.add(neighbor)
            mutations+=1        
        return -1