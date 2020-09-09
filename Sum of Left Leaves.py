# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
            
        res = []
        def rec(root,s,flag):
            
            if root:
                if not root.left and not root.right and flag==0:
                    s+=root.val
                    res.append(s)
                rec(root.left,s,0)
                rec(root.right,s,1)
        rec(root,0,0)     
        return sum(res)
                
            
        
        
        
