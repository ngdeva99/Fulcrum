class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==0:
            return 0
        memo=[]
        memo.append(0)
        memo.append(nums[0])
        print(memo)

        for i in range(2,len(nums)+1):

            memo.append(max(memo[i-2]+nums[i-1],memo[i-1]))

        print(memo)
        return memo[len(memo)-1]
    
