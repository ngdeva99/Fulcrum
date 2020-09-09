"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        if not head:
            return head
        
        
        node = dummy = Node(0)
        
        stack = [head]
        
        while stack:
            
            curr = stack.pop()
            
            if curr.next:
                stack.append(curr.next)
                
            if curr.child:
                stack.append(curr.child)
                
            node.next = curr
            
            curr.prev = node
            
            curr.child = None
            
            node = curr
            
        res = dummy.next
        res.prev = None
        return res
