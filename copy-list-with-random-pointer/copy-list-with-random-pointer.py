"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {None:None}
        
        #First, we will make a copy of a old node and saved them in a dictionary
        curr = head
        while(curr!=None):
            
            copy = Node(curr.val)
            oldToNew[curr]=copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]
        

        

        
   