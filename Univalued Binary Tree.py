# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        a = []
        def rec(root):
            
            if root:
                a.append(root.val)
                rec(root.left)
                rec(root.right)
                
        rec(root)
        
        return 1 == len(set(a))
