class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        
        adj = {}
        
        for i in arr:
            if i in adj:
                adj[i]+=1
                
            else:
                adj[i]=1
                
        a = set(adj.values())
        return len(a)==len(adj)
