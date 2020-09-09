class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ans = 0
        ans
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans = max(self.dfs(grid,i,j),ans)
                    

                    
        return ans
        
    def dfs(self,grid,i,j):
        
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0
        
        if grid[i][j]!=1:
            return 0

        grid[i][j]=2
        return 1+self.dfs(grid,i+1,j)+self.dfs(grid,i-1,j)+self.dfs(grid,i,j+1)+self.dfs(grid,i,j-1)    
                    
        
