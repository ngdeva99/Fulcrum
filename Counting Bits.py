class Solution:
    def countBits(self, num: int) -> List[int]:
        
        res = []
        for i in range(num+1):
            
            count=0
            while(i):
                
                count+=(i&1)
                i>>=1
                
            res.append(count)
            
        return res
        
