class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        
        precompute = [i for i in range(1,n**2+1)]
        print(precompute)
    
        count = 0
        res =[[0]*n for _ in range(n)]
        
        visited = [[False]*n for _ in range(n)]
        
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        
        rr,cc,di =0,0,0
        
        r,c = len(res),len(res[0])
        
        for i in range(n**2):
            
            res[rr][cc] = precompute[count]
            count+=1
            visited[rr][cc] =  True
            
            cr,ccc = rr+dr[di],cc+dc[di]
            
            if 0<=cr<r and 0<=ccc<c and not visited[cr][ccc]:
                
                rr,cc = cr,ccc
                
            else:
                
                di = (di+1)%4
                rr,cc = rr+dr[di],cc+dc[di]
                
        return res
