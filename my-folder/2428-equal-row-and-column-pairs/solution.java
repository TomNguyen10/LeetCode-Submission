class Solution {
    public int equalPairs(int[][] grid) {
        Map<String, Integer> map = new HashMap<>();
        for (int r = 0; r < grid.length; r++) {
            StringBuilder sb = new StringBuilder();
            for (int c = 0; c < grid[0].length; c++) {
                sb.append(grid[r][c]);
                sb.append('+');
            }
            String s = sb.toString();
            map.put(s, map.getOrDefault(s, 0) + 1);
        }
        int res = 0;
        for (int c = 0; c < grid[0].length; c++) {
            StringBuilder sb = new StringBuilder();
            for (int r = 0; r < grid.length; r++) {
                sb.append(grid[r][c]);
                sb.append('+');
            }
            String s = sb.toString();
            if (map.containsKey(s)) {
                res += map.get(s);
            }
        }
        return res;
    }
}
