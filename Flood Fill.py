class Solution:
    def floodFill(self, A: List[List[int]], sr: int, sc: int, nc: int) -> List[List[int]]:
        
        color = A[sr][sc]
        if color==nc:
            return A
        self.dfs(A,sr,sc,color,nc)
        return A
        
        
        
        
    def dfs(self,A,i,j,num,nc):
        
        if i<0 or j<0 or i>=len(A) or j>=len(A[0]):
            return 
        
        if A[i][j]==num:
            A[i][j] = nc
            self.dfs(A,i+1,j,num,nc)
            self.dfs(A,i-1,j,num,nc)
            self.dfs(A,i,j+1,num,nc)
            self.dfs(A,i,j-1,num,nc)
