class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y, grid):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == "0":
                return
            grid[y][x] = "0"
            dfs(x+1, y, grid)
            dfs(x-1, y, grid)
            dfs(x, y+1, grid)
            dfs(x, y-1, grid)
        
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfs(c, r, grid)
        
        return count
