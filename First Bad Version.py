# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        beg = 1
        last = n
        
        while beg<last:
            
            mid = beg+((last-beg)//2)
            
            if(isBadVersion(mid)):
                last = mid
            
            else:
                beg = mid + 1
            
                
        return beg          
        
