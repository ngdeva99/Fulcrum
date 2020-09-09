class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        if amount==0:
            return 0

        
        
        dp = [100005]*(amount+1)
        dp[0] = 0
        for i in range(1,len(dp)):
            
            for x in coins:
                
                if i-x>=0:
                    
                    dp[i] = min(dp[i-x]+1,dp[i])
                   

        if dp[amount]==0 or dp[amount]==100005:
            return -1
        return dp[amount]

        
