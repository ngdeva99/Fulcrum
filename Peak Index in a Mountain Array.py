class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        beg,end = 0,len(nums)-1
        if len(nums)==0:
            return -1
        
        if len(nums)==1:
            return 0
        
        if len(nums)==2:
            return 0 if nums[0]>nums[1] else 1
        
        while beg<end:
            
            mid = beg + (end-beg)//2
            
            if nums[mid]<nums[mid+1]:
                beg = mid+1
            else:
                end = mid
        
        return beg
