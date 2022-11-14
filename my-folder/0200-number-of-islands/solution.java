class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        int n = grid.length;
        int m = grid[0].length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == '1') {
                    DFS (grid,i,j);
                    ++count;
                }
            }
        }

        return count;
    }

    private void DFS (char[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0';

        DFS (grid, i+1, j);
        DFS (grid, i-1, j);
        DFS (grid, i, j+1);
        DFS (grid, i, j-1);
    }
}
