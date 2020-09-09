class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        m = {}
        
        for l in ransomNote:
            if l in m:
                m[l]+=1
            else:
                m[l]=1
        
        for l in ransomNote:
            if m[l] > magazine.count(l):
                return False
        return True
    
        
