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
    


    def union(self,x,y,timeStmp):
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
    
    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
        logs.sort(key=lambda row:row[0])
        for i in range(len(logs)):
            x = logs[i][1]
            y = logs[i][2]
            timestmp = logs[i][0]
            self.union(x,y,timestmp)
            if self.count == 1:
                return timestmp
            
        return -1
        