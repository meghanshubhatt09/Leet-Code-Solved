# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        queue = []
        queue.append(root)
        res = []
        
        while (queue):
            ans = []
            n = len(queue)
            for i in range(n):
                x = queue.pop(0)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
                ans.append(x.val)
            res.append(ans)
        return res
            
            
        