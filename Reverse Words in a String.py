class Solution:
    def reverseWords(self, s: str) -> str:
        

        s = s.split(" ")
        
        s = [i for i in s if len(i)>0]
        
        if len(s)<=1:
            return "".join(s)
        
        
        
        res = [""]*len(s)
        
        l,r = 0,len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            res[l] = s[l]
            res[r] = s[r]
            l+=1
            r-=1
        res[l] = s[l]
        return " ".join(res)
            
        
        
