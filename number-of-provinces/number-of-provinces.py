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
    
    # The union function with union by rank
    def union(self, x, y):
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

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.root = [i for i in range(len(isConnected))]
        self.rank = [1] * len(isConnected)
        self.count = len(isConnected)
        
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                
                if isConnected[r][c] == 1:
                    self.union(r,c)
        return self.count
                    
        
        
        