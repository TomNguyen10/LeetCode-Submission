class Solution {
    public int[][] findFarmland(int[][] land) {
        int rows = land.length;
        int cols = land[0].length;
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (land[i][j] == 1) {
                    int[] temp = new int[]{i, j};
                    dfs(land, j, i, temp);
                    int[] arr = new int[]{i, j, temp[0], temp[1]};
                    list.add(arr); 
                }
            }
        }
        int[][] res = new int[list.size()][4];
        for (int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        return res;
    }

    private void dfs(int[][] land, int x, int y, int[] arr) {
        if (x < 0 || x >= land[0].length || y < 0 || y >= land.length || land[y][x] == 0) {
            return;
        }
        arr[0] = Math.max(arr[0], y);
        arr[1] = Math.max(arr[1], x);
        land[y][x] = 0;
        dfs(land, x+1, y, arr);
        dfs(land, x-1, y, arr);
        dfs(land, x, y+1, arr);
        dfs(land, x, y-1, arr);
    }
}
