class Solution:
    def divisorGame(self, N: int) -> bool:
        
        if N==2:
            return True
        elif N==1:
            return False
        
        dp =[]
        dp.append(True)
        dp.append(True)
        dp.append(True)
        print(dp)
        for i in range(3,N+1):
            if i%2!=0:
                dp.append(not(dp[i-1]))
            else:
                dp.append((dp[i-1]^dp[i-2]))
        print(dp)
        return dp[N]
        
        
