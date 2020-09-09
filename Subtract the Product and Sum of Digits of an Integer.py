class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        
        a = [int(d) for d in str(n)]
        return (prod(a)-sum(a))
