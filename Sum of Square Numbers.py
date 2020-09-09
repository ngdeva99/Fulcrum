class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        
        x = []
        
        a = math.floor(math.sqrt(c))
        

        x = [pow(d,2) for d in range(a+1)]
        
        
        left = 0 
        right = len(x)-1
        
        while left<=right:
            calc=x[left]+x[right]
            if calc==c:
                return True
            elif calc<c:
                left = left +1
            elif calc>c:
                right =right -1
        return False
                
