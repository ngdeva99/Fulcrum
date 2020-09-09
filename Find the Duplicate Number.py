class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        nums.sort() #nlogn
        
        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]:
                return nums[i]
                
        
