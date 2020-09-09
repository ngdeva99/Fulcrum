# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, target):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        a = []
        inorder(root,a)
        
        leftptr = 0
        rtptr = len(a)-1
        
        while leftptr < rtptr:
            
            calc = a[leftptr]+a[rtptr]
            
            if calc == target:
                
                return True
            
            elif calc<target:
                
                leftptr = leftptr + 1
            
            elif calc>target:
                rtptr = rtptr - 1
                
        return False
        
def inorder(root,a):
    
    if root:
        
        inorder(root.left,a)
        
        #print(root.val)
        a.append(root.val)
        
        inorder(root.right,a)
        
        
