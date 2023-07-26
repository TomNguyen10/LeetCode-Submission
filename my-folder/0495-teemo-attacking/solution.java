class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int res = 0;
        int start = timeSeries[0];
        int end = timeSeries[0] + duration;
        for (int i = 1; i < timeSeries.length; i++) {
            if (timeSeries[i] > end) {
                res += end - start;
                start = timeSeries[i];
            }
            end = timeSeries[i] + duration;
        }
        res += end - start;
        return res;
    }
}
