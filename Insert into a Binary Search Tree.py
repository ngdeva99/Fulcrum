# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        
       
        def rec(root):
        
            if root.val<val:
                if not root.right:
                    root.right= TreeNode(val)
                else:
                    rec(root.right)

            elif root.val>val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    rec(root.left)

        rec(root)
        
        return root
        
