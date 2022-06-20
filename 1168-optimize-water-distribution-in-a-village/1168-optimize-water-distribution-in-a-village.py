class Solution:
    def __init__(self):
        self.root = []
        self.rank = []
        
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return False
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.root[rootX] < self.root[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootX] += 1
            return True
        
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        self.root = [i for i in range(n+1)]
        self.rank = [1] * (n+1)
        
        ordered_edges = []
        # adding a virtual vertex for joining wells edges
        
        for index, weight in enumerate(wells):
            ordered_edges.append((weight,0,index+1))
            
        for house1, house2, weight in pipes:
            ordered_edges.append((weight,house1,house2))
            
        # sort the entire edges by their weights
        ordered_edges.sort(key=lambda x: x[0])
        
        total_cost = 0
        for cost, house1, house2 in ordered_edges:
            if self.union(house1,house2):
                total_cost+=cost
        return total_cost
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        