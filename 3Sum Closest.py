class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(closest):
                    closest = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if closest == 0:
                break
        print(closest)
        return target - closest
