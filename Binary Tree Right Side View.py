# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        
        res = []
        self.dfs(root,0,res)
        return [x[0] for x in res]
        
    def dfs(self,root,level,res):
        
        if root:
            if len(res)<level+1:
                res.append([])

            res[level].append(root.val)
            self.dfs(root.right,level+1,res)
            self.dfs(root.left,level+1,res)
