class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(grid, row, col):
            seen = [False] * 10
            for i in range(3):
                for j in range(3):
                    num = grid[row+i][col+j]
                    if num < 1 or num > 9:
                        return False
                    if seen[num]:
                        return False
                    seen[num] = True
            
            row1 = grid[row][col] + grid[row][col+1] + grid[row][col+2]
            row2 = grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2]
            row3 = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]

            col1 = grid[row][col] + grid[row+1][col] + grid[row+2][col]
            col2 = grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1]
            col3 = grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2]

            dg1 = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
            dg2 = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]

            if row1 != row2 or row2 != row3: return False

            if col1 != col2 or col2 != col3: return False

            if dg1 != dg2: return False

            return True
        
        res = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if check(grid, i, j):
                    res += 1

        return res
