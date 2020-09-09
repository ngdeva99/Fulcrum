class Solution:
    def hammingWeight(self, n: int) -> int:
        a = 0
        while n>0:
            a+=1
            n = n & n-1
        return a
        
