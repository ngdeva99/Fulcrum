class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        
        ans = 0
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                
                if i==0 or j==0 or i==len(A)-1 or j==len(A[0])-1:
                    self.dfs(A,i,j)
            
        for i in range(len(A)):
            for j in range(len(A[0])):
                
                if A[i][j]==1:
                    ans+=1
        
        return ans
        
        
        
        
    def dfs(self,A,i,j):
        
        if i<0 or j<0 or i>=len(A) or j>=len(A[0]):
            return 
        
        if A[i][j]!=1:
            return
        
        A[i][j] = -1
        self.dfs(A,i+1,j)
        self.dfs(A,i-1,j)
        self.dfs(A,i,j+1)
        self.dfs(A,i,j-1)
        
        
