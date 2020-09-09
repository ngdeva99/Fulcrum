class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        
        
        ### Top down approach with memoization
        
        
        
        def calc(A,i,j,dp):
            
            if i==len(A) or j==len(A[0]):
                return float('inf')
            
            if i==len(A)-1 and j==len(A[0])-1:
                if A[i][j]>0:
                    return 1
                return abs(A[i][j])+1
            
            if dp[i][j]!=0:
                return dp[i][j]
            
            else:
                dp[i][j] = max(1,min(calc(A,i+1,j,dp),calc(A,i,j+1,dp))-A[i][j])
                return dp[i][j]
            
            
        dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        
        return calc(dungeon,0,0,dp)
        
