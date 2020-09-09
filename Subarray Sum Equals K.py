class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        d = {}
        d[0] = 1
        s = 0
        count = 0
        for i in range(len(nums)):
            
            s += nums[i]
            if s-k in d: # --- I
                count += d[s-k]
                # or return True
                # or return indicies

            #dd sum to frq dict
            if s in d:
                d[s] += 1 # --- II
            else:
                d[s] = 1
        print(d)
        return count
