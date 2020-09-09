class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left =0 
        right = len(s)-1
        
        while left<right:
            if s[left]!=s[right]:

                #return True if isPal(s,left+1) or isPal1(s,right-1) else #TODO
                if isPal(s[left:right]) or isPal(s[left+1:right+1]):
                    return True

                return False

            left+=1
            right-=1
        return True
            
def isPal(s):
        left=0
        right = len(s)-1
        
        while left<right:
            
            if s[left]!=s[right]:
                return False
            
            left+=1
            right-=1
        return True
    
def isPal1(s,right):

        left=0

        while left<right:

            if s[left]!=s[right]:
                return False

            left+=1
            right-=1
        return True
