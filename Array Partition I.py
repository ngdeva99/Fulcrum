class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        left = 0
        right = left+1
        su = 0
        while left<=len(nums)-2:
            su +=min(nums[left],nums[right])
            left+=2
            right+=2
        return su
