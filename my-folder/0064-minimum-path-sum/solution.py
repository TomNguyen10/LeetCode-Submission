class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows == cols == 1:
            return grid[0][0]
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for r in range(rows):
            for c in range(cols):
                val = grid[r][c]
                if r == 0 and c > 0:
                    dp[r][c] = dp[r][c-1] + val
                elif c == 0 and r > 0:
                    dp[r][c] += dp[r-1][c] + val
                else:
                    dp[r][c] = min(val + dp[r-1][c], val + dp[r][c-1])
        
        return dp[rows-1][cols-1]
