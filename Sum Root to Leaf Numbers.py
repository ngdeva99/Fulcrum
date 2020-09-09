# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        res = []
        def rec(root,path):
            
            if root:
                
                new_path = 10*path+root.val
                
                if root.right or root.left:
                    a = rec(root.left,new_path)
                    b = rec(root.right,new_path)
                    
                    
                    return a+b
                else:
                    res.append(new_path)
                    
                    return new_path
            else:
                
                return 0
        
        k=rec(root,0)
        return sum(res)
