class Solution:
    def addDigits(self, num: int) -> int:
        
        if len(str(num))==1:
            return num
        a = [int(d) for d in str(num)]
        return self.addDigits(sum(a))
        
