class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        q =[]
        color ={}
        
        for i in range(len(graph)):
            
            if i not in color:
                
                color[i]=0

                q.append(i)
                
                while len(q)!=0:
                    
                    root = q.pop(0)
                    
                    for node in graph[root]:
                        if node not in color:
                            color[node]= 1-color[root]
                            q.append(node)
                            
                        else:
                            if color[node]==color[root]:
                                return False
                            
        return True
                
                        
                
        
