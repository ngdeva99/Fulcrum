class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        if target in nums:
            return [nums.index(target),nums.index(target)+(nums.count(target))-1]
        return [-1,-1]
        
