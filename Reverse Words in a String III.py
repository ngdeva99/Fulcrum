class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split(" ")
        res = []
        for i in s:
            i = i[::-1]
            res.append(i)
            
        return " ".join(res)
        
        
        
