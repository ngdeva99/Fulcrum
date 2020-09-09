class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num = {}
        
        for ind, x in enumerate(nums):
            
            y = target - x
            
            if y in num:
                
                return [num[y],ind]
            
            else:
                
                num[x] = ind
                
        return []
                

