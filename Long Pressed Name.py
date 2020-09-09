class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        
        i=0
        j=0
        
        while i<len(name) and j<len(typed):
            
            if name[i]==typed[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==len(name):
            return True
        return False
