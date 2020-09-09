class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        f1 = f2 = 0
        for x in reversed(cost):
            print(f1,f2)
            f1, f2 = x + min(f1, f2), f1
            print(f1,f2)
        return min(f1, f2)
            
        
