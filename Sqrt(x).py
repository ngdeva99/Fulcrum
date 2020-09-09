class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==1 or x==0:
            return x
        
        curr = x//2 + 1
        
        next = x//2
        
        while curr>next:
            curr = next
            next = (curr + x//curr)//2
            
        return curr
        
