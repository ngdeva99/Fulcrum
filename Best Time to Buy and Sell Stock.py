class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #one pass solutuion
        
        if len(prices)==0:
            return 0
        mini = max(prices)
        maxi = 0
        
        
        for i in prices:
            if i < mini:
                mini = i
            
            elif i - mini > maxi:
                maxi = i-mini
            
        return maxi    
            
        
