class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = []
        time,fresh = 0,0
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append([i,j])
                    
        while (len(queue)!=0 and fresh > 0):

            for i in range(len(queue)):
                r,c = queue.pop(0)

                for ra,ca in direction:
                    rx = r + ra
                    ry = c + ca
                    if rx < 0 or rx >= row or ry < 0 or ry >= col or grid[rx][ry]!=1:
                        continue
                    grid[rx][ry] = 2
                    fresh -= 1
                    queue.append([rx,ry])
            time += 1

        return time if fresh==0 else -1
                    
                
        
        
        
                    
                    
                
        
        
        
        
        
        