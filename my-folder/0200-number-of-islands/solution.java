class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, j, i);
                }
            }
        }
        return count;
    }

    void dfs(char[][] grid, int x, int y) {
        if (x < 0 || x >= grid[0].length || y < 0 || y >= grid.length || grid[y][x] != '1') {
            return;
        }
        grid[y][x] = '0';
        dfs(grid, x+1, y);
        dfs(grid, x-1, y);
        dfs(grid, x, y+1);
        dfs(grid, x, y-1);
    }
}
