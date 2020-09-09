class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # worst soln O(n)
        
        if target in nums:
            return nums.index(target)
            
        else:
            return -1
