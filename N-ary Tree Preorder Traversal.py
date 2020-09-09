"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        
        res  = []
        
        if root is None:
            return res
        
        
        def rec(root,res):
            
            res.append(root.val)
            
            for c in root.children:
                rec(c,res)
                
        rec(root,res)
        return res
