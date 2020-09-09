# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        
        
        queue = [root,"null"]
        res = [[]]
        a = [x,y]
        level = 0
        
        while len(queue)!=0:
             
            curr = queue.pop(0)
            
            
            if curr:
                if curr!="null":
                    print(curr.val)
                    if curr.val in a:
                        u = queue[0] 
                        if u:
                            if u!="null":
                                if u.val in a:
                                    if queue[1] and queue[1]!="null":
                                        return True
                                    return False
                            
                    res[level].append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                
                elif curr=="null" and len(queue)!=0:
                    res.append([])
                    level+=1
                    queue.append("null")
                    
                
                    
        for i in res:
            if len(i)==0:
                res.remove(i)
        print(res)        
        for i in res:
            if len(i)==1:
                continue
            
            else:
                if x in i and y in i:
                    return True
        
                    
        return False
