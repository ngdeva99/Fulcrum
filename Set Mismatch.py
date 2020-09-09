class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        m={}
        
        for i in nums:
            if i in m:
                y=i
            else:
                m[i]=1
        
        x = ((len(nums))*(len(nums)+1))//2 - sum(nums)
        return [y,y+x]
