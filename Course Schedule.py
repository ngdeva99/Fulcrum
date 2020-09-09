class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        
        
        if len(pre)==0:
            return [i for i in range(n)]

        
        if len(pre)==1:
            pre = pre[0]
            return pre[::-1]
        
        
        ##############
        visited = [False]*n
        cycle = [False]*n
        
        res = []
        
        adj = {}
        a = []
        
        
        ##############
        
        #Creation of adjecency matrix
        for i in pre:
            if i[1] in adj:
                adj[i[1]].append(i[0])
                
            else:
                adj[i[1]] = [i[0]]
        print(adj)
        for i in range(n):
            if i not in adj:
                a.append(i)
        print(a)
        
        
        ###############
        
        
        
        for i in range(n):
            if not visited[i]:
                if self.dfs(i,adj,visited,cycle,res) is True:
                    return []
        #remaining stuffs not in pre
        res = list(set(res))
        return res[::-1]
        
        #####################
        
        
    def dfs(self,root,adj,visited,cycle,res):
        
        ######
        #cycle detection
        
        if not visited[root]:
            visited[root] = True
            cycle[root] = True
            if root in adj:
                for node in adj[root]:
                    if not visited[node]:
                        if self.dfs(node,adj,visited,cycle,res) is True:
                            return True

                    elif cycle[node]==True:
                        return True
  
        cycle[root] = False
        ########
        
        res.append(root)
        return False
