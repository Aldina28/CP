class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = {}; self.vis = set()
        for i in range(len(equations)):
            a = equations[i][0]; b = equations[i][1] 
            val = values[i]
            if a not in self.graph:
                self.graph[a] = {}
                self.graph[a][a] = 1
            if b not in self.graph:
                self.graph[b] = {}
                self.graph[b][b] = 1
            self.graph[a][b] = val
            self.graph[b][a] = 1/val

        
        def dfs(source,target,val):
            if source==target:
                self.val = val
                return
            self.vis.add(source)
            for next,multiplier in self.graph[source].items():
                if next not in self.vis:
                    dfs(next,target,val*multiplier)

        
        output = []
        for a,b in queries:
            print(a,b)
            self.val = -1.0; self.vis = set()
            if a not in self.graph or b not in self.graph:
                output.append(-1)
            else:    
                dfs(a,b,1)
                output.append(self.val)
        return output
         
                 