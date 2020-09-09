class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        
        
        arr.sort()
        b=[]
        print(arr)
        dp = [arr[i]-arr[i-1] for i in range(1,len(arr))]
        print(dp)
        
        x  = min(dp)
        for i in range(1,len(arr)):
            if dp[i-1]==x:
                 b.append([arr[i-1],arr[i]])
        return b
        
         
        
