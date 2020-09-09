class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        for letter in s:
            if letter in left:
                stack.append(letter)
            elif letter in right:
                if len(stack) <= 0:
                    return False
                if left.index(stack.pop()) != right.index(letter):
                    return False
        return len(stack) == 0
