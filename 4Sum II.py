class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        
        m = {}
        for a in A:
            for b in B:
                
                if a+b in m:
                    m[a+b]+=1
                else:
                    m[a+b] = 1
                
        ways =0
        
        for a in C:
            for  b in D:
                
                if -(a+b) in m:
                    
                    ways += m[-(a+b)]                  
                else:
                    continue
        return ways
