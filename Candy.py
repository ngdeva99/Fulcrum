class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        """  
        ##BRute force
        
        flag = True
        
        candies = [1]*len(ratings)
        
        while flag:
            
            flag = False
            
            for i in range(len(ratings)):
                
                if i!=len(ratings)-1 and ratings[i]>ratings[i+1] and candies[i]<=candies[i+1]:
                    
                    candies[i] = candies[i+1]+1
                    flag = True
                
                if i>0 and ratings[i]>ratings[i-1] and candies[i]<=candies[i-1]:
                    
                    candies[i] = candies[i-1]+1
                    flag = True
        
        
        return sum(candies)
    
        """
    
    ## O(n) | O(n) two pass soln
    
    
        l2r = [1]*len(ratings)
        r2l = [1]*len(ratings)
        
        
        
        for i in range(len(ratings)-1):
            if ratings[i]>=ratings[i+1]:
                l2r[i+1]=1
                
            else:
                l2r[i+1]=l2r[i]+1
                
                
                
        for i in range(len(ratings)-1,0,-1):
            if ratings[i]>=ratings[i-1]:
                r2l[i-1]=1
                
            else:
                r2l[i-1]=r2l[i]+1
        
        
        for i in range(len(ratings)):
            l2r[i] = max(l2r[i],r2l[i])
            
        return sum(l2r)
            
            
        
    
