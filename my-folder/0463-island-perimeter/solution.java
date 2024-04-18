class Solution {
    public int islandPerimeter(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int res = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                res += 4*grid[i][j];
                if (i > 0) {
                    res -= grid[i][j]*grid[i-1][j];
                }
                if (i < r-1) {
                    res -= grid[i][j]*grid[i+1][j];
                }
                if (j > 0) {
                    res -= grid[i][j]*grid[i][j-1];
                }
                if (j < c - 1) {
                    res -= grid[i][j]*grid[i][j+1];
                }
            }
        }
        return res;
    }
}

