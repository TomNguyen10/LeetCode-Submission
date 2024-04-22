class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
        int prev = intervals[0][1];
        int res = 0;
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] < prev) {
                res++;
            }
            else {
                prev = intervals[i][1];
            }
        }
        return res;
    }
}
