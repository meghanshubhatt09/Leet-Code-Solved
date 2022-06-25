class Solution:
    def __init__(self):
        self.root = []
        self.cost = 0
        self.rank = []
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self,w, x, y):
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
            self.cost += w
            return True
        
            
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        self.root = [i for i in range(len(points))]
        weights = []
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                distance = abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1])
                weights.append([distance,i,j])
                
        weights.sort()
        edges_used = 0
        self.rank = [1 for i in range(len(self.root))]
        for i in range(len(weights)):
            if self.union(weights[i][0],weights[i][1],weights[i][2]):
                edges_used+=1
                if edges_used == len(points)-1:
                    break
        
        return self.cost
        
        
                
        