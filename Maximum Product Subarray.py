class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        ans=cmin=cmax=nums[0]
        
        for i in nums[1:]:
            
            cmin,cmax = min(i,cmin*i,cmax*i),max(i,cmin*i,cmax*i)
            
            if cmax>ans:
                ans = cmax
                
        return ans
            
            
        
