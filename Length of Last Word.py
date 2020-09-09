class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        s = s.split(" ")
        print(s)
        s =[i for i in s if len(i)>0]
        print(s)
        if len(s)>0:
            return len(s[-1])
        return 0
