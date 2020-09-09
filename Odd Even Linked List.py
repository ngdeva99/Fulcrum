# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        
        if not head:
            return None
        odd = head
        even = head.next
        evenhead = even
        
        #even for odd nos and even.next for even nos
        
        while even is not None and even.next is not None:
            
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
            
            
        odd.next = evenhead
        
        return head
        
