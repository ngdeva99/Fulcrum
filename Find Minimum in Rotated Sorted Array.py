class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        
        b,e = 0,len(nums)-1
        while b<e:
            m=b + (e-b)//2
            
            if nums[m]>nums[e]:
                b = m+1
            else:
                e =m
                
        return nums[b]
