class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        lsb = n&1
        
        while(n!=0):
            
            n = n>>1
            x = lsb^(n&1)
            
            if x==0:
                return False
            
            lsb = n&1
            
        return True
