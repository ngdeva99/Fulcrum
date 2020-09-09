# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        
        if root is None:
            return 0
        
        queue = [root,"null"]
        
        res = [[]]
        level = 0
        
        while len(queue)!=0:
            
            curr = queue.pop(0)
            
            if curr:
                
                if curr!="null":
                    
                    res[level].append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                    
                elif curr=="null" and len(queue)!=0:
                    level+=1
                    res.append([])
                    queue.append("null")
                    
            else:
                continue
                
        for i in res:
            if len(i)==0:
                res.remove(i)
                
        res = [sum(i) for i in res]
        
        return res.index(max(res))+1
