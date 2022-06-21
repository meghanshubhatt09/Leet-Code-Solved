"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        oldToNew = {}
        
        def cloneDFS(node):
            
            if node in oldToNew:
                return oldToNew[node]
            
            new_copy = Node(node.val)
            oldToNew[node] = new_copy
            
            for neigh in node.neighbors:
                new_copy.neighbors.append(cloneDFS(neigh))
            return new_copy
        
        return cloneDFS(node) if node else None
        

        

            