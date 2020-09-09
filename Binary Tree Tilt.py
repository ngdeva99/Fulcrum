# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        
        self.tilt = 0
        
        k = self.traverse(root)
        print(k)
        return self.tilt
    
    def traverse(self,root):
        
        if root is None:
            return 0
        
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        print(l,r)
        self.tilt += abs(l-r)
        return l+r+root.val
    
    
