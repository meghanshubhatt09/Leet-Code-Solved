from collections import deque
class Solution:
    

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]
        if grid[0][0] == 1 or grid[-1][-1]==1:
            return -1
        row = len(grid)
        col = len(grid[0])
        
        queue = deque()
        queue.append([0,0,1])
        
        
        
        
        while(len(queue)!=0):
            r,c,count= queue.popleft()
            
            if r == len(grid)-1 and c == len(grid)-1:
                return count
                
            count += 1
            for ra, ca in directions:
                rx = r + ra
                ry = c + ca
                
                if rx < 0 or ry < 0 or rx >= len(grid) or ry >= len(grid) or grid[rx][ry] == 1:
                    continue
                else:
                    grid[rx][ry] = 1
                    queue.append([rx,ry,count])
                    
                    
        return -1
                    
                
 

        
        
        

            
            
        
        