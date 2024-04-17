class Solution {
    public int maxProfit(int[] prices) {
        int minPurchase = prices[0];
        int maxProfit = 0;
        for (int i = 1; i < prices.length; i++) {
            maxProfit = Math.max(maxProfit, prices[i] - minPurchase);
            minPurchase = Math.min(minPurchase, prices[i]);
        }
        return maxProfit;
    }
}
