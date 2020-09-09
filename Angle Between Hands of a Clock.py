class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        
        
        degm = 6*minutes
        degh = 0.5*minutes
        print(degh,degm)
        
        k = abs(degm-((hour%12)*30)-degh)
        if k>180:
            return 360-k
        return k
