class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        b,e = 0,len(nums)-1
        
        while b<=e:
            
            m = b+((e-b)//2)
            
            if nums[m]==target:
                return m
            
            elif nums[m]>target:
                e=m-1
                
            else:
                b=m+1
                
        return -1
        
