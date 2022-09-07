class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))]for _ in range(len(grid)) ]
        count = 0
        
        row = len(grid)
        col = len(grid[0])
        
        def DFS(grid, r, c):
            
            if r < 0 or r >= row or c < 0 or c >= col or visited[r][c] == True or grid[r][c]=='0':
                return
            visited[r][c] = True
            DFS(grid,r-1,c)
            DFS(grid,r+1,c)
            DFS(grid,r,c-1)
            DFS(grid,r,c+1)
            
            
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and visited[r][c] == False:
                    count += 1
                    DFS(grid,r,c)
                
        return count
                
        
        
        