class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""

        for i in range(len(s)):
            
            t = self.help(s,i,i)
            
            if len(t)>len(res):
                res = t
                
            u = self.help(s,i,i+1)
            
            if len(u)>len(res):
                res = u
                
        return res
    
    def help(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:

            l-=1
            r+=1
        return s[l+1:r]
