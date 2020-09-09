# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
    
        def dfs(node, prefix):
            if node:
                new_prefix = node.val + 2*prefix

                if node.left or node.right:
                    return dfs(node.left, new_prefix) + dfs(node.right, new_prefix)
                else:
                    return new_prefix
            else:
                return 0

        return dfs(root, 0)
