class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        print([s.count(c)//2*2 for c in set(s)])
        counts = sum([s.count(c)//2*2 for c in set(s)])
        print(counts)
        return counts + 1*(counts<len(s))
            
            
