class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num ==0 or num==1:
            return True
        elif num<=3 and num>1:
            return False
        
        a = sqrt(4*num)/2
        
        return floor(a)==ceil(a)
