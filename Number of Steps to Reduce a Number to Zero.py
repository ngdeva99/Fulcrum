class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        count = 0
        while num!=0:
            print(num,count)
            if num==1:
                count+=1
                return count
                
            if num%2==0:
                count+=1
            else:
                count+=2
            num = num>>1

