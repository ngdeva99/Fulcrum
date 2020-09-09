# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        
        p = head
        length =1
        
        while p.next:
            p = p.next
            length+=1
            
        rotate = k%length
        
        if k==0 or rotate ==0:
            return head
        
        slow = fast = head
        
            
        for i in range(rotate):
            fast = fast.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        slow.next = None
        fast.next = head
        
        head = temp
        
        return head
