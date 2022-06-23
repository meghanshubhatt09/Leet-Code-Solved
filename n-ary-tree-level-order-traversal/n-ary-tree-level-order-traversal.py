"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        queue1 = []
        queue1.append(root)
        queue2 = []
        result = []
        
        
        while(len(queue1)!=0 or len(queue2)!=0):
            path = []
            while(len(queue1)!=0):
                
                u = queue1.pop(0)
                path.append(u.val)
                
                for neigh in u.children:
                    queue2.append(neigh)
            
            if len(path) > 0:
                result.append(path)
                
            
            path2 = []
            while(len(queue2)!=0):
                
                p = queue2.pop(0)
                path2.append(p.val)
                
                for neigh in p.children:
                    queue1.append(neigh)
            
            if len(path2) > 0:
                result.append(path2)
            
            
                
        return result
                
            
        