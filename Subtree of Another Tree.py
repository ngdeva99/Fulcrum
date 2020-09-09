# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def rec(s,t):
            if s is None and t is None:
                return True
        
            if s is None or t is None:
                return False
        
            return s.val==t.val and rec(s.left,t.left) and rec(s.right,t.right)
        
        return s is not None and (rec(s,t) or self.isSubtree(s.left,t) or self
            .isSubtree(s.right,t))
