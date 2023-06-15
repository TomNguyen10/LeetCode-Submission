class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) return 0;
        int i = 0;
        int j = 1;
        int max = 0;
        while (j < prices.length) {
            if (prices[i] < prices[j]) {
                max = Math.max(max, prices[j] - prices[i]);
            }
            else {
                i = j;
            }
            j++;
        }
        return max;
    }
}
