class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        if len(nums)==1:
            return True
        jump = 0
        
        maxReach = steps = nums[0]
        if maxReach==0:
            return False
        
        
        for i in range(1,len(nums)):
            
            if maxReach>=len(nums)-1:
                return True
            
            maxReach = max(maxReach,nums[i]+i)
            steps-=1
            
            
            if steps==0:
                
                jump+=1
                steps = maxReach-i
                
                if steps==0:
                    return False
                
        return False
