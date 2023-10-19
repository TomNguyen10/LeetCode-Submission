class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] min = new int[n];
        min[0] = cost[0];
        min[1] = cost[1];
        for (int i = 2; i < n; i++) {
            min[i] = cost[i] + Math.min(min[i-1], min[i-2]);
        }
        return Math.min(min[n-1], min[n-2]);
    }
}

