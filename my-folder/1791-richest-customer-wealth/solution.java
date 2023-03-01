class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for (int r = 0; r < accounts.length; r++) {
            int total = 0;
            for (int c = 0; c < accounts[0].length; c++) {
                total += accounts[r][c];
            }
            if (total > max)
                max = total;
         }
        return max;
    }
}
