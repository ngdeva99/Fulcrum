class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ways=0
        for k in nums:
            if len(str(k))%2==0:
                ways+=1
            else:
                continue
        return ways
