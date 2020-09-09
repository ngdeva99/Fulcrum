# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        small = root.val
        res = []
        def rec(root):
            if root:
                rec(root.left)
                res.append(root.val)
                rec(root.right)
            
        rec(root)
        
        res = set(res)
        if len(res)==1:
            return -1
        res = [i for i in res]
        print(res)
        
        res = [i-small for i in res]
        print(res)
        
        
        max = 0
        for i in res:
            if i==0:
                res.remove(i)
        
        print(res)
        return min(res)+small
