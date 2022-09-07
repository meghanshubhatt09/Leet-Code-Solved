# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBT(root, left_min, right_max):
            
            if not root:
                return True
            
            if not (root.val > left_min and  root.val < right_max):
                return False
            
            return (validateBT(root.left,left_min, root.val)
                   and validateBT(root.right,root.val, right_max))
        
        return validateBT(root, float('-inf'), float('inf'))

        
        
        