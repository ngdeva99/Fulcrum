# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        num1,num2 = 0,0
        
        while l1 or l2:
            if l1:
                num1 = num1*10+l1.val
                l1 = l1.next
            if l2:
                num2 = num2*10+l2.val
                l2 = l2.next
                
        dummy = node = ListNode(0)
        
        
        for num in str(num1+num2):
            newnode = ListNode(int(num))
            
            if not dummy.next:
                dummy.next = tail = newnode
            else:
                tail.next = newnode
                tail = tail.next
        
        return node.next
