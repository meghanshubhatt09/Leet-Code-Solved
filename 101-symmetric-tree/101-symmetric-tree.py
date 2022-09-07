# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def checkSym(self,left, right):
        
        if (left == None or right == None):
            return left == right
        
        if left.val != right.val:
            return False
        
        return (self.checkSym(left.left, right.right) and self.checkSym(left.right, right.left))
        
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.checkSym(root.left, root.right)
    
        