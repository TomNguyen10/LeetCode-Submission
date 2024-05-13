class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)

        winner = 0

        for opponent in range(n):
            if opponent == winner:
                continue
            if grid[winner][opponent] == 0:
                winner = opponent
        
        return winner
