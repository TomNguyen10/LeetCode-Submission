class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sums = 0;
        for (int i = 0; i < k; i++) {
            sums += nums[i];
        }
        double max = (double) sums/k;
        for (int i = k; i < nums.length; i++) {
            sums = sums - nums[i-k] + nums[i];
            max = Math.max(max, (double) sums/k);
        }
        return max;
    }
}
