class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if len(grid)==0:
            return 0
        visited = [[False]*len(grid[i]) for i in range(len(grid))]
        

        ans = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and not visited[i][j]:
                    ans+=1
                    self.dfs(grid,i,j,visited)
                    #literally its the no of times u r redirected here with some nodes being unvisited in dfs
                    
        return ans
    
    def dfs(self,grid,i,j,visited):
        
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 
    
        if grid[i][j]!='1' or visited[i][j]:
            return 
        
        visited[i][j]=True
        self.dfs(grid,i+1,j,visited)
        self.dfs(grid,i-1,j,visited)        
        self.dfs(grid,i,j+1,visited)
        self.dfs(grid,i,j-1,visited)        
