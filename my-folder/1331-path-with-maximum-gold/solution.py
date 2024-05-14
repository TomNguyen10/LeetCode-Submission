class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            temp = grid[i][j]
            grid[i][j] = 0

            max_gold = 0
            for dx, dy in directions:
                max_gold = max(max_gold, backtrack(i + dx, j + dy))

            grid[i][j] = temp

            return max_gold + temp

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, backtrack(i, j))

        return max_gold
