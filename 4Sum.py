class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                
                l,r = j+1,len(nums)-1
                
                while l<r:
                    
                    calc = nums[i]+nums[j]+nums[l]+nums[r]
                    
                    if calc==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        
                    elif calc>target:
                        r-=1
                        
                    elif calc<target:
                        l+=1
                        
        if len(res)==1:
            return res
        
        fin_soln=[]
        
        for i in range(len(res)):
            flag=1
            for j in range(0,i):
                if res[i]==res[j]:
                    flag=0
                    break
            if flag==1:       
                fin_soln.append(res[i])
        
        return fin_soln
                    
