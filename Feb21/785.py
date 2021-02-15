    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        color = {}
        def dfs(current):
            for elem in graph[current]:
                if elem in color:
                    if color[elem] == color[current]:
                        return False
                
                else:
                    color[elem] = 1 + color[current]
                    if not dfs(elem):
                        return False
            return True
                    
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
