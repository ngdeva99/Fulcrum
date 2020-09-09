class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        a = float('inf')
        ans = a
        sum1=0
        left = 0
        
        for i in range(len(nums)):
            
            sum1+=nums[i]
            
            while sum1>=s:
                
                ans = min(ans,i-left+1)
                sum1-= nums[left]
                left+=1
                
        return ans if ans!=a else 0
        
