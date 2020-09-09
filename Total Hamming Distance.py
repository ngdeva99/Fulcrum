class Solution:
    def totalHammingDistance(self, arr: List[int]) -> int:
        
        arr=sorted(arr)
        
        #same as sum of two diff bits in an array of integers
        
        ans = 0  # Initialize result 
        n = len(arr)
        # traverse over all bits 
        for i in range(0, 32): 
          
            # count number of elements with i'th bit set 
            count = 0
            for j in range(0,n): 
                if ( (arr[j] & (1 << i)) ): 
                    count+=1
            # Add "count * (n - count) *" to the answer 
            ans += (count * ((n - count))); 
            print(count,ans)

        return ans
