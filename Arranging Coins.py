class Solution:
    def arrangeCoins(self, n: int) -> int:
        
       #O(1) solution
    
        if n==0:return 0
        if n==1:return 1
        
        return int(-1+math.sqrt((1+8*n)))//2
