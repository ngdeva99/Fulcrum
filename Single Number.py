class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        num = {}
        
        for i in nums:
            if i in num:
                num[i]+=1
            else:
                num[i]=1
                
        for index,value in num.items():
            if value==1:
                return index
        
        
