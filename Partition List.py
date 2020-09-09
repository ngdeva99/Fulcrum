# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        
        before = beforehead = ListNode(0)
        after = afterhead =ListNode(0)
        
        while head:
            
            if head.val<x:
                before.next = head
                before = before.next
                
            else:
                after.next = head
                after = after.next
                
            head = head.next
        
        after.next = None
        
        before.next = afterhead.next
        
        return beforehead.next
        
