# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        res = []
        def rec(root):
            if root:
                rec(root.left)
                res.append(root.val)
                rec(root.right)
        rec(root)
        print(res)
        if len(res)==2:
            if res[0]>=res[1]:
                return False
        if len(res)==1:
            return True
        if len(res)==0:
            return True
        
        
        for i in range(len(res)-1):
            print(res[i],res[i+1])
            if res[i]>=res[i+1]:
                return False
        
        return True

