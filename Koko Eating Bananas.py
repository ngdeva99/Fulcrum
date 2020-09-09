class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        if len(piles)==0:
            return 0
        
        l,r = 1,pow(10,9)
        
        while l<=r:
            
            m = (l+r)>>1
            
            sum = 0
            for i in piles:
                sum+=(i+m-1)//m
                
            if sum<=H:
                r = m-1
                
            else:
                l = m+1
                
        return l
        
        
