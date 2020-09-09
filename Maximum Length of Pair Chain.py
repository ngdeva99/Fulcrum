class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
        a = {}
        for i in pairs:
            a[(i[0],i[1])]=sum(i)
                
        a = sorted(a.items(), key=lambda kv: kv[1])
        a = [list(i[0]) for i in a]
        print(a)
        dp = [1]*len(pairs)
        
        for i,k in enumerate(a):
            for j in range(i):
                
                if a[i][0]>a[j][1]:
                    
                    dp[i] = max(dp[i],dp[j]+1)
                    
        return max(dp)
