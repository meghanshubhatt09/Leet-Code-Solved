# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        
        def makePath(root,x,path):
            if root is None:
                return False
            
            path.append(root)
            
            if root == x:
                return True
            
            if (makePath(root.left,x,path) or makePath(root.right,x,path)):
                return True
            
            path.pop(-1)
            return False
            

        
        if (makePath(root,p,path1) == False or makePath(root,q,path2) == False):
            return -1
        i = 0
        while(i < len(path1) and i < len(path2)):
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]
        
        

            
        