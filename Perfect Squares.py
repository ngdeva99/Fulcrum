class Solution:
    def numSquares(self, n: int) -> int:
        
        if n==0:
            return 0
            
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        c = n
        n = int(sqrt(n))
        a = [i**2 for i in range(1,n+1)]
        
        for i in range(1,len(dp)):
            for j in a:
                
                if i-j>=0:
                    
                    dp[i] = min(dp[i-j]+1,dp[i])
        print(dp)
        if dp[n]==float('inf'):
            return -1
        return dp[c]
        
