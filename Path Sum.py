# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = []
        def rec(root,path):
            
            if root:
                
                new_path = path+root.val
                
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
        print(res)
        for i in res:
            if i==sum:
                return True
        return False 
        
        
