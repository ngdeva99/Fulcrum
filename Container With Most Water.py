class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        maxarea = 0
        l,r=0,len(height)-1
        
        while l<r:
            
            maxarea = max(maxarea,(r-l)*min(height[l],height[r]))
            
            if height[l]<height[r]:
                l+=1
                
            else:
                r-=1
                
        return maxarea
    
        
