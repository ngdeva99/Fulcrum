# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def rec(root, val):
            if root:
                root.val += rec(root.right, val)
                return rec(root.left,root.val)
            else:
                return val
            
        rec(root,0)
        return root
                
    
        
