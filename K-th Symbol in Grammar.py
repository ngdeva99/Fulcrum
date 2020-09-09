class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        if N==1:
            return 0
        
        else:
            
            if K%2==0:
                
                return 0 if self.kthGrammar(N-1,(K+1)//2) else 1
            else:
                return 1 if self.kthGrammar(N-1,(K+1)//2) else 0
        
