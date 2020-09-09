class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        A.sort()
        B=[]
        print(A)
        for x in range(len(A)-2):
            
            if A[x]+A[x+1]>A[x+2]:
                B.append(A[x]+A[x+1]+A[x+2])
            
            else:
                B.append(0)
                
        return max(B)

