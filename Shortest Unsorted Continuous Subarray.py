class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        a = nums[:]
        a = sorted((a))
        
        l,r = len(nums),0
        
        for i in range(len(nums)):
            
            if nums[i]!=a[i]:
                l = min(l,i)
                r = max(r,i)
                
        return r-l+1 if r-l>0 else 0
