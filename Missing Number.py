class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        m = max(nums)
        
        if m!=0:
            
            nums = list(set([x for x in range(m+1)]) - set(nums))
            print(len(nums))
            if len(nums)!=0:
                for x in nums:
                    return x
            else:
                return m+1
        elif m==0:
            return 1
