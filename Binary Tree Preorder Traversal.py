# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
                #Morris PreOrder Traversal
        
        
        curr = root
        res = []
        
            
        while curr is not None:
            
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            
            else:
                p = curr.left
                
                while p.right is not None and p.right is not curr: 
                    p = p.right 
                    
                if not p.right:
                    p.right = curr
                    res.append(curr.val)
                    curr = curr.left
                else:
                    p.right = None
                    
                    curr = curr.right
        
        return res
        
