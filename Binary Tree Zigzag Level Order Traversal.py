# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        queue = [root,"null"]
        res = [[]]
        
        if not root:
            return 
        level =0
        while len(queue)!=0:
            curr = queue.pop(0)
            
            if curr:
                if curr!="null":
                    res[level].append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
                        
                elif curr=="null" and len(queue)!=0:
                    res.append([])
                    queue.append("null")
                    level+=1
        
        for i in res:
            if len(i)==0:
                res.remove(i)
        print(res)
        res = [i[::-1] if res.index(i)%2!=0 else i for i in res]
        return res
        
