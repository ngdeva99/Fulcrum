class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        if len(word1)==0 or len(word2)==0:
            return max(len(word1),len(word2))
        
        if len(word1)==0 and len(word2)==0:
            return 0
        
        dp = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        for j in range(len(word1)+1):
            dp[0][j] = j
            
        for i in range(len(word2)+1):
            dp[i][0] = i
        print(dp,len(dp),len(dp[0]))
        
        
        for i in  range(1,len(dp)):
            for j in range(1,len(dp[0])):
                
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                    
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                    
        return dp[len(dp)-1][len(dp[0])-1]
