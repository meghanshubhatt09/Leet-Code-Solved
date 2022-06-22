class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph)-1
        results = []
        
        def backstrack(currNode,path):
            if currNode == target:
                results.append(list(path))
                return
            
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backstrack(nextNode,path)
                path.pop()
                
        
        path = deque([0])
        backstrack(0,path)
        
        return results