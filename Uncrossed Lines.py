class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if len(A)==0 or len(B)==0:
            return 0
    
        dp = [[0 for _ in range(len(A)+1)]for _ in range(len(B)+1)]
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
            
                if A[j-1]==B[i-1]:
                    
                    dp[i][j] = 1+dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]
