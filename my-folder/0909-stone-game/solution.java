class Solution {
    public boolean stoneGame(int[] piles) {
        int n = piles.length;
        int[][] dp = new int[n][n];
        for (int i = 0; i < n; i++) {
            dp[i][i] = piles[i];
        }
        for (int r = 1; r < n; r++) {
            for (int c = 0; c < n - r; c++) {
                dp[c][r+c] = Math.max(piles[c] - dp[c+1][c+r], piles[c+r] - dp[c][c + r - 1]);
            }
        }
        return dp[0][n-1] > 0;
    }
}
