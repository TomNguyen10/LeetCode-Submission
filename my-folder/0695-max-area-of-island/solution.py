class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def dfs(grid, row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            res = 1
            res += dfs(grid, row - 1, col)
            res += dfs(grid, row + 1, col)
            res += dfs(grid, row, col - 1)
            res += dfs(grid, row, col + 1)
            return res
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(grid, r, c)
                    max_area = max(area, max_area)
        
        return max_area
