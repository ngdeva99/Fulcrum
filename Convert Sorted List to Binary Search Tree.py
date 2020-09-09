# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next       
        
        
        def ToBST(nums):
            if len(nums)==0:
                return None

            mid = len(nums)//2

            root = TreeNode(nums[mid])

            root.left = ToBST(nums[:mid])
            root.right =ToBST(nums[mid+1:])

            return root
        
        return ToBST(nums)
