# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        dummy = node = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            node.next = temp
            head = head.next
            node = temp.next
            
        return dummy.next
            
        
