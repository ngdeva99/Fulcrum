class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        b,e = 0 ,len(nums)-1
        
        while b<e:
            
            m = b + (e-b)//2
            
            if nums[m]<nums[e]:
                e = m
                
            else:
                if nums[m]==nums[e]:
                    e -=1
                else:
                    b = m+1
                
            
        return nums[b]
