import itertools
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
                
        ans = []
        backtrack(0, len(nums))
        ans = [list(t) for t in set(map(tuple, ans))]
                
        return ans
            
