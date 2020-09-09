class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n
        res = []

        for i in range(len(graph)):
            if self.dfs(graph, i, color):
                res.append(i)

        return res

    def dfs(self, graph, start, color):
        
        if color[start] == 2:
            return False
        elif color[start] == 1:
            return True

        color[start] = 2

        for end in graph[start]:
            if not self.dfs(graph, end, color):
                return False

        color[start] = 1

        return True
                
                    
        
        
        
        
