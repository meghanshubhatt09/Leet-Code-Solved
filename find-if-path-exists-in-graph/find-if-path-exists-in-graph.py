class Solution:
    def __init__(self):
        self.visited = []
        
    def DFS(self,start,adj_list,destination):
        self.visited[start] = True
        if start == destination:
            return True
        for i in (adj_list[start]):
            if self.visited[i] == False:
                if self.DFS(i,adj_list,destination) == True :
                    return True
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.visited = [False] * n
        adj_list = [[] for i in range(n)]
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        for i in range(n):
            if self.visited[i] == False:
                if self.DFS(source,adj_list,destination) == True:
                    return True
        return False
        
        