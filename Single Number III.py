class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # "xor" all the nums 
        tmp = 0
        for num in nums:
            tmp ^= num
        # find the rightmost "1" bit
        i = 0
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
        # compute in two seperate groups
        first, second = 0, 0
        for num in nums:
            if num & tmp:
                first ^= num
            else:
                second ^= num
        return [first, second]

