class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        if len(nums)==0:
            return 0
        mx = max(nums)
        print(mx)
        left,right = 1,mx
        
        while left<=right:
            
            mid = (left+right)>>1
            
            sum = 0
            for i in nums:
                sum+=(i+mid-1)//mid
                
            if sum<=threshold:
                right = mid-1
                
            else:
                left = mid+1
                
        return left
