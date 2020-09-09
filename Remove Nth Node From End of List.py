# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        
        slow = fast = head
        count = 0
        flag = False
        while fast and fast.next:
            count+=1
            
            if count-n>0:
                flag = True
                slow = slow.next
                fast = fast.next
            
            else:
                fast = fast.next

        if slow.next is None:
            
            return None
        
        
        
        
        if flag==True or (count==1 and n==1):
            
            if slow.next.next is None:
                slow.next = None
            
            else:
                slow.next = slow.next.next
            
            
        elif count-n==0:
            
            slow.next = slow.next.next
            
            
        else:
            
            slow = slow.next
            head = slow
                  
                
                
                
        return head

