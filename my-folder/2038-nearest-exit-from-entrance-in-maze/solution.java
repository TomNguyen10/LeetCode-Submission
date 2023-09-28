class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int rows = maze.length;
        int cols = maze[0].length;
        int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        maze[entrance[0]][entrance[1]] = '+';

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{entrance[0],entrance[1], 0});

        while (!queue.isEmpty()) {
            int[] currState = queue.poll();
            int curRow = currState[0];
            int curCol = currState[1];
            int curDistance = currState[2];

            for (int[] dir : dirs) {
                int nextRow = curRow + dir[0];
                int nextCol = curCol + dir[1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols && maze[nextRow][nextCol] == '.') {

                    if (nextRow == 0 || nextRow == rows - 1 || nextCol == 0 || nextCol == cols - 1) {
                        return curDistance + 1;
                    }
                    maze[nextRow][nextCol] = '+';
                    queue.offer(new int[]{nextRow, nextCol, curDistance+1});
                }
            }
        }

        return -1;
    }
}
