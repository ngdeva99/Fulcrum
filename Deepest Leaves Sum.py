# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        depth = self.maxDepth(root)-1
        level = 0
        res =[[]]
        
        q = [root,"null"]
        
        while len(q)!=0:
            
            curr = q.pop(0)
            
            if curr:
                
                if curr!="null":
                    
                    res[level].append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
                    
                elif curr=="null" and len(q)!=0:
                    res.append([])
                    level+=1
                    q.append("null")
                    
        for i in res:
            if len(i)==0:
                res.remove(i)
                
        return sum(res[-1])
        
        
    def maxDepth(self,root):
        
        if root is None:
            return 0
        
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            
        return max(l,r)+1
