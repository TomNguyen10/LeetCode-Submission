class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));
        int arrow = 1;
        int start = points[0][0];
        int end = points[0][1];

        for (int i = 1; i < points.length; i++) {
            int xStart = points[i][0];
            int xEnd = points[i][1];

            if (xStart <= end) {
                start = xStart;
            }
            else {
                arrow++;
                start = xStart;
                end = xEnd;
            }
        }
        return arrow;
    }
}