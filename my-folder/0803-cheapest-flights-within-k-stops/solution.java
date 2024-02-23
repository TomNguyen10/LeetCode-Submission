class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[src] = 0;

        for (int i = 0; i <= k; i++) {
            dp = updateMinCost(flights, dp);
        }

        return dp[dst] == Integer.MAX_VALUE ? -1 : dp[dst];
    }

    private int[] updateMinCost(int[][] flights, int[] dp) {
        int[] temp = dp.clone();

        for (int[] flight : flights) {
            int from = flight[0];
            int to = flight[1];
            int price = flight[2];

            if (dp[from] < Integer.MAX_VALUE) {
                temp[to] = Math.min(temp[to], dp[from] + price);
            }
        }

        return temp;
    }
}

