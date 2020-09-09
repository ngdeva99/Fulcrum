class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        
        if len(bloomDay)==0 or m==0 or k==0:
            return 0
        
        if m*k > len(bloomDay):
            return -1
        
        left,right = float('inf'),float('-inf')
        
        for i in bloomDay:
            left = min(left,i)
            right = max(right,i)
            
        while left<=right:
            mid = (left+right)>>1
            
            if self.isValid(bloomDay,m,k,mid):
                right = mid-1
                
            else:
                left = mid+1
                
        return left
    
    def isValid(self,bloomDay,m,k,mid):
        
        count,size = 0,0
        for i in bloomDay:
            
            if i<=mid:
                size = size+1
            
            else:
                size = 0
                
            if size ==k:
                size = 0
                count+=1
                
            if count ==m:
                return True
            
        return False

