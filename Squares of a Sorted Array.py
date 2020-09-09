class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        res = [None]*len(A)
        left,right = 0,len(A)-1
    
        for i in range(len(A)-1,-1,-1):
            
            if abs(A[left])>abs(A[right]):
                
                res[i] = A[left]**2
                left+=1
                
            else:
                
                res[i] = A[right]**2
                right-=1
                
        return res
                
