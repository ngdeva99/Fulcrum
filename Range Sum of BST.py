# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        a=[]
        inorder(root,a)
        a = a[a.index(L):a.index(R)+1]
        return sum(a)
def inorder(root,a):
    
    if root:
        
        inorder(root.left,a)
        
        a.append(root.val)
        
        inorder(root.right,a)
