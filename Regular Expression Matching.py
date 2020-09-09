class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        dp[0][0] = True
        
        #noT ALWAYS COLMNS ARE FALSE BECAUSE SOMETIMES THEY CAN match with the empty string for cases like a*b* 
            patterns with "" string.
        
        #Deals with patterns like a* or a*b* or a*b*c*
        for j in range(1,len(dp[0])):
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2]

                
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                if s[i-1]==p[j-1] or p[j-1]==".":
                    
                    dp[i][j] = dp[i-1][j-1]
                    
                elif p[j-1]=="*":
                    dp[i][j] = dp[i][j-2]
                    
                    if s[i-1]==p[j-2] or p[j-2]==".":
                        dp[i][j] |= dp[i-1][j]  

                else:
                    dp[i][j] = False
        print(dp)            
        return dp[-1][-1]
