# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None: return []
        
        queue1 = []
        queue2 = []
        
        queue1.append(root)
        res = []
        
        while(len(queue1) != 0 or len(queue2)!= 0):
            
            ans1 = []
            while(queue1):
                x = queue1.pop()
                if x.left: queue2.append(x.left)
                if x.right: queue2.append(x.right)
                ans1.append(x.val)
            
            if ans1:
                res.append(ans1)
            
            ans2 = []
            while(queue2):
                x = queue2.pop()
                if x.right: queue1.append(x.right)
                if x.left: queue1.append(x.left)
                    
                ans2.append(x.val)
                
            
            if ans2:
                res.append(ans2)
                
        return res
            
            

            
            
        
        