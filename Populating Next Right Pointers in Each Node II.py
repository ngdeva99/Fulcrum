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
        
        self.root_node = root       # make a copy to return the result
        kid = temp = Node(0)        # kid is ptr for traversing the child level, temp 
            is dummy ptr to just store kid starting position
        while root:
            while root:
                if root.left:
                    kid.next = root.left
                    kid = kid.next
                if root.right:
                    kid.next = root.right
                    kid = kid.next
                root = root.next
            root, kid = temp.next, temp
            kid.next = None         # Reset the chain for temp
        return self.root_node

            
        
            
            
            
                
    
        
        
