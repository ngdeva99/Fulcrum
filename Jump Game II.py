class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ## This is the general approach O(n2) time | O(n) space
        """
        dp = [float('inf')]*(len(nums))
        
        dp[0] = 0
        
        for i in range(1,len(dp)):
            for j in range(i):
                
                if j+nums[j]>=i:
                    
                    dp[i] = min(dp[i],dp[j]+1)
                    
        return dp[-1]
        """
        
        
        ## This is the optimized solution
        
        if len(nums)==1:
            return 0
        
        maxReach = steps = nums[0]
        jumps = 0 
        
        for i in range(1,len(nums)):
            
            if i==len(nums)-1:
                return jumps+1
            
            maxReach = max(maxReach,i+nums[i])
            steps-=1
            
            print(maxReach,steps)
            if steps==0:
                
                jumps+=1
                steps = maxReach-i
