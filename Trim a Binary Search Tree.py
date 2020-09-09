# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        def rec(root):
            
            if not root:
                return None
            
            elif root.val<L:
                return rec(root.right)
                
            elif root.val>R:
                return rec(root.left)
            
            else:
                root.left = rec(root.left)
                root.right = rec(root.right)
                return root
        return rec(root)
