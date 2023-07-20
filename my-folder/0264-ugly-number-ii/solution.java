class Solution {
    public int nthUglyNumber(int n) {
        int[] uglys = new int[n];
        uglys[0] = 1;
        int p2 = 0, p3 = 0, p5 = 0;
        for (int i = 1; i < n; i++) {
            int mini = Math.min(uglys[p2] * 2, Math.min(uglys[p3] * 3, uglys[p5] * 5));
            uglys[i] = mini;
            if (uglys[p2] * 2 == mini) {
                p2++;
            }
            if (uglys[p3] * 3 == mini) {
                p3++;
            }
            if (uglys[p5] * 5 == mini) {
                p5++;
            }
        }
        return uglys[n-1];
    }
}
