class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows == cols == 1:
            return grid[0][0]

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c ==0:
                    continue
                elif r == 0 and c > 0:
                    grid[r][c] += grid[r][c-1]
                elif c == 0 and r > 0:
                    grid[r][c] += grid[r-1][c]
                else:
                    grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        print(grid)
        return grid[rows-1][cols-1]
