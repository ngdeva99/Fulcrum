class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = ""
        k = 0
        for i in range(len(s)):
            
            t,k = self.help(s,i,i,k)
            
            if len(t)>len(res):
                res = t
                
            u,k = self.help(s,i,i+1,k)
            if len(u)>len(res):
                res = u
                
        return k
    
    def help(self,s,l,r,count):
        while l>=0 and r<len(s) and s[l]==s[r]:
            count+=1
            l-=1
            r+=1
        return s[l+1:r],count
