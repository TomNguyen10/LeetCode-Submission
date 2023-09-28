class Solution {
    public int orangesRotting(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        Queue<int[]> queue = new LinkedList<>();
        int count = 0;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == 2) {
                    queue.offer(new int[]{r, c, 0});
                }
                else if (grid[r][c] == 1) {
                    count++;
                }
            }
        }

        int min = 0;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int curRow = curr[0];
            int curCol = curr[1];
            min = curr[2];

            for (int[] dir : directions) {
                int newRow = curRow + dir[0]; // Use curRow here
                int newCol = curCol + dir[1]; // Use curCol here

                if (newRow >= 0 && newRow < row && newCol >= 0 && newCol < col && grid[newRow][newCol] == 1) {
                    grid[newRow][newCol] = 2; 
                    count--;
                    queue.offer(new int[]{newRow, newCol, min + 1});
                }
            }
        }

        return count > 0 ? -1 : min; // Return -1 if count is greater than 0, otherwise, return min
    }
}

