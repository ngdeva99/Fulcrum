class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        
        num={"U":0,"D":0,"L":0,"R":0}
        for c in moves:
            if c in num:
                num[c]+=1
                
        if num["U"]==num["D"] and num["L"]==num["R"]:
            return True
        return False

