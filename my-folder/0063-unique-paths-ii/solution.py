class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1:
            return 0
        dp = [[0 for _ in range(cols)] for _ in range(rows)] 
        dp[0][0] = 1
        for i in range(1, rows):
            if grid[i][0] == 1:
                dp[i][0] = 0
            else:
                dp[i][0] += dp[i-1][0]
        for i in range(1, cols):
            if grid[0][i] == 1:
                dp[0][i] = 0
            else:
                dp[0][i] += dp[0][i-1]
                
        for r in range(1, rows):
            for c in range(1, cols):
                if grid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[rows-1][cols-1]
