"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 
        'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        startroot = root
        
        while startroot and startroot.left:
            
            self.populate(startroot)
            startroot = startroot.left
        
        return root
        
    def populate(self,root):
        
        while root is not None:
            
            root.left.next = root.right
            
            if root.next is not None:
                
                root.right.next = root.next.left
                
            root = root.next
            
    
        
        
        
