class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        if len(weights)==0:
            return 0
        
        left,right  = max(weights),sum(weights)
        
        
        
        while left<=right:
            count = 0
            
            m = (left+right)>>1
            
            sum1 = 0
            for i in weights:
                
                sum1+=i
                
                if sum1 >= m:
                    count+=1
                    
                    if sum1 > m:
                        sum1 = i
                        
                    else:
                        sum1 = 0
                        
            if sum1!=0:
                count+=1
                
            if count<=D:
                right = m-1
                
            else:
                left = m+1
                
        return left
                
