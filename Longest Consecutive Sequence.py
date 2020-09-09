class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        
        if len(nums)==1:
            return 1
        
        nums = sorted(nums)
        print(nums)
        if len(nums)==2:
            if abs(nums[0])-abs(nums[1])==1:
                return 2
            return 1
        
        
        size = 0
        
        dp = [1]*len(nums)
        
        for i in range(1,len(dp)):
            for j in range(i):
                
                if nums[i]==nums[j]+1:
                    dp[i] = max(dp[j]+1,dp[i])
                    
        return max(dp)
