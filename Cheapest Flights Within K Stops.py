class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        #bellmann ford algorithm
        
        #### what i tried
        """
        maxi = 1000005
        dist = [maxi]*(n+1)
        
        dist[src] = 0
        
        res = 0
        count =0
        for i in range(K+1):
            count = 0
            for j in range(len(flights)):
                
                
                u = flights[j][0]
                v = flights[j][1]
                w = flights[j][2]
                
                if v==dst:
                    count+=1
                    if u==src:
                        count-=1
                        
                        
                print(dist[u],dist[v],u,v,count)
                if dist[u]!=maxi and ((dist[u]+w)<dist[v]) and count<=K:
                    dist[v] = dist[u]+w
                    
                elif count>K:
                    dist[v] = dist[v]
                    count-=1
                    
                else:
                    dist[v] = dist[v]
                        
                        
        print(dist)
        
        if dist[dst]==maxi:
            return -1
        return dist[dst]

        """
 
        costs = [float('inf')] * n
        costs[src] = 0

        for _ in range(K+1):
            copy = costs[:]
            for s, d, w in flights:
                copy[d] = min(copy[d], costs[s] + w)
            costs = copy

        return -1 if costs[dst] == float('inf') else costs[dst]
