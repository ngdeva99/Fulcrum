class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        
        n = len(times)
        if not n:
            return 0
        
        maxi = 1000005
        
        dist = [maxi]*(N+1)
        res = 0
        dist[K] = 0
        
        for i in range(N):
            for j in range(n):
                
                u = times[j][0]
                v = times[j][1]
                w = times[j][2]
                
                if (dist[u]!=maxi) and ((dist[u]+w)<dist[v]):
                    
                    dist[v] = dist[u] + w

        for i in range(1,N+1):
            res = max(res,dist[i])
            
        print(dist,res)        
        if res!=maxi:
            return res
        
        return -1
