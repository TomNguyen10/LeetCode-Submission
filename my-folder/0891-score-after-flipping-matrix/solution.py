class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def transformRow(arr):
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = 1
                else:
                    arr[i] = 0
        
        def transformCol(c):
            for r in range(len(grid)):
                if grid[r][c] == 0:
                    grid[r][c] = 1
                else:
                    grid[r][c] = 0
        
        for i in range(len(grid)):
            row = grid[i]
            if row[0] == 0:
                transformRow(row)
        
        for c in range(len(grid[0])):
            zeros = 0
            ones = 0
            for r in range(len(grid)):
                if grid[r][c] == 0:
                    zeros += 1
                else:
                    ones += 1
            if zeros > ones:
                transformCol(c)
        
        score = 0
    
        for row in grid:
            score += int(''.join(map(str, row)), 2)
    
        return score

