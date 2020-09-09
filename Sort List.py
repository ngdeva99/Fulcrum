# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res = []
        dummy = node = ListNode(0)
        while head is not None:
            res.append(head.val)
            head = head.next
        
        res = sorted(res)
        print(res)
        
        for i in res:
            node.next = ListNode(i)
            node = node.next
        
        return dummy.next
