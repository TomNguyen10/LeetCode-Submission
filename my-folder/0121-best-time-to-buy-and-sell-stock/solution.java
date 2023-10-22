class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int left = 0;
        int right = 1;
        while (right < prices.length) {
           if (prices[left] < prices[right]) {
               int profit = prices[right] - prices[left];
               res = Math.max(profit, res);
           }
           else {
               left = right;
           }
           right++;
        }
        return res;
    }
}
