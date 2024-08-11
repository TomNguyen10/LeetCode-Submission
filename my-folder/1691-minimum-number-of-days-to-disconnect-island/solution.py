class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visited):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return
            visited.add((r, c))
            dfs(r+1, c, visited)
            dfs(r-1, c, visited)
            dfs(r, c+1, visited)
            dfs(r, c-1, visited)
        
        def count():
            visited = set()
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        dfs(i, j, visited)
                        count += 1
            return count

        if count() != 1: return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count() != 1: return 1
                    grid[i][j] = 1
        
        return 2
            
