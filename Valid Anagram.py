class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        m = {}
        
        if len(s)==0 and len(t)==0:
            return True
        
        if len(s)!=len(t):
            return False

        for i in s:
            if i in m:
                
                m[i]+=1
                
            else:
                m[i]=1
                
        s1 = False    
        
        for i in t:
            if i in m and t.count(i)==s.count(i):
                s1=True
            else:
                return False

        print(1^1)
        
        return s1
            
            
        
