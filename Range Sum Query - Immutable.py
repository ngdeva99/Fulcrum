class NumArray:

    def __init__(self, nums: List[int]):

        if not nums:
            return
        
        self.dp=[0 for i in nums]
        self.dp[0]=nums[0]
        for i in range(1,len(nums)):
            self.dp[i]=nums[i]+self.dp[i-1]
            
        print(self.dp)
    

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.dp[j]
        return self.dp[j]-self.dp[i-1]
