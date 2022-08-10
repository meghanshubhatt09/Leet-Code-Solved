import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        def Euclidean(x,y):
            o = math.sqrt((x-0)**2 + (y-0)**2)
            return o
        
        my_array = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            
            dist = Euclidean(x,y)
            my_array.append([dist,i])

          
        heapq.heapify(my_array)
        res = []
        
        for i in range(k):
            val = heapq.heappop(my_array)
            res.append(points[val[1]])
        return res
            
        
            
            

            

            
        
        
        