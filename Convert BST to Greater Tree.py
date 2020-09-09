# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def change(root, val):
            if root:
                root.val += change(root.right, val)
                return change(root.left,root.val)
            else:
                return val
            
        change(root,0)
        return root
