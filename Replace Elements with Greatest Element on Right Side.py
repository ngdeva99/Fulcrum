class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            
            if i==len(nums)-1:
                nums[i] = -1
                continue
                
            nums[i] = max(nums[i+1:])
        
        return nums
