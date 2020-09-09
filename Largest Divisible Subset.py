class Solution:
    def largestDivisibleSubset(self, nums):
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((s+[n] for s in dp if not s or n % s[-1] == 0), key=len))
        return max(dp, key=len)
