class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return new int[0][];
        }
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));
        List<int[]> res = new ArrayList<>();
        res.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] prev = res.get(res.size() - 1);
            int[] curr = intervals[i];
            if (prev[1] >= curr[0]) {
                prev[1] = Math.max(prev[1], curr[1]);
            }
            else {
                res.add(curr);
            }
        }

        return res.toArray(new int[res.size()][]);
    }
}
