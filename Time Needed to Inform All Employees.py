class Solution:
    max_time = 0
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        global max_time
        max_time=0

        def dfs(adj,node,path_sum):
            global max_time

            if adj.get(node)==None:
                max_time=max(max_time,path_sum)
                return 

            else:
                for i in adj[node]:
                    dfs(adj,i,path_sum+informTime[node])



        adj={}

        for i in range(len(manager)):

            if adj.get(manager[i])!=None:
                adj[manager[i]].append(i)

            else:
                adj[manager[i]]=[i]
        max_path=0

        dfs(adj,headID,0)

        return max_time
        
