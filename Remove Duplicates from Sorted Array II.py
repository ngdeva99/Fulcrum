class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 2
        fp = 2
        
        while i<len(nums):
            
            if nums[i]!=nums[fp-1] or nums[i]!=nums[fp-2]:
                
                nums[fp] = nums[i]
                fp+=1
            i+=1
        
        return fp
                
        
