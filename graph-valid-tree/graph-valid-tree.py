class Solution:
    def __init__(self):
        self.root = []
        self.rank = []
        self.count = 0
        
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
        else:
            return False
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
        
        for i in range(len(edges)):
            x = edges[i][0]
            y = edges[i][1]
            
            if self.union(x,y) == False:
                return False
        print(self.count)
        if self.count != 1:
            return False
        return True
            
        
        