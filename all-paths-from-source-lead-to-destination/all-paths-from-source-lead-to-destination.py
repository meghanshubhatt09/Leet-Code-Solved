class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        def buildGraph(n,edges):
            g = {i:set() for i in range(n)}
            for a,b in edges:
                g[a].add(b)
            return g
        
        def backstack(src,dest):
            if not graph[src]:
                if src == dest:
                    return True
                return False
            
            for i, neighbour in enumerate(graph[src]):
                if visited[src][i]==True:
                    return False
                else:
                    visited[src][i]=True
                    res = backstack(neighbour,dest)
                    
                    if res is False:
                        return False
                    
                    visited[src][i]=False
                    
            return True
        
                    
                
        
        graph = buildGraph(n,edges)
        visited = { i: [False] * len(graph[i]) for i in range(n) }
        return backstack(source,destination)

            
            
            
            
     
