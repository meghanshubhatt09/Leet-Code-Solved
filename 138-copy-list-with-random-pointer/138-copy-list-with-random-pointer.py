"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def __init__(self):
        self.visitHash = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None
        
        if head in self.visitHash:
            return self.visitHash[head]
        
        
        node = Node(head.val,None,None)
        
        self.visitHash[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
        

        
   