# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """ 
        
        if not head or not head.next:
            return head
        
        # FINDING MIDDLE ELEMENT
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        curr = slow.next
        slow.next = None
        
        prev = None
        
        #Reversing 2nd half
        
        while curr:
            
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = head   
        
        #keeping curr pointer at l1 and prev pointer at 5 in 4 <-5 and then shifting the strings
        while prev:
            
            temp = prev.next
            prev.next = curr.next
            curr.next = prev
            curr = curr.next.next
            prev = temp
            
        return head
            
            
        
        
