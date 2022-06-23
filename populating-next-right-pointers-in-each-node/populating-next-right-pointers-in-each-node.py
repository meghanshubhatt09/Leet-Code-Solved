"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        

                
            
        
        queue = []
        queue.append(root)
        
        if not root:
            return root
        
        while(len(queue)!=0):
            size_of_Queue = len(queue)
            
            for i in range(size_of_Queue):
                ms = queue.pop(0)
                if i < size_of_Queue-1:
                    ms.next = queue[0]
                
                if ms.left != None:
                    queue.append(ms.left)
                    
                if ms.right != None:
                    queue.append(ms.right)
            
        return root

        



        
        



            
                    
        
            
        
        