class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        
        
        l,r = 0,target
        
        min_diff = float('inf')
        ans = 0
        
        while l<=r:
            
            m = (l+r)>>1
            
            sum = 0
            
            for i in arr:
                
                if i<m:
                    sum+=i
                else:
                    sum+=m
                    
            if sum==target:
                return min(m,max(arr))
            
            if (abs(sum-target) <  min_diff):
                min_diff = abs(sum-target)
                ans = m
                
            if sum<=target:
                l = m+1
            
            else:
                r = m-1
        print(ans)
        return min(max(arr),ans)
                
                    
        
