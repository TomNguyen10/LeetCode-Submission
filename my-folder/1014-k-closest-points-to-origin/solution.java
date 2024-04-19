class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] p1, int[] p2) {
                double distance1 = Math.sqrt(p1[0] * p1[0] + p1[1] * p1[1]);
                double distance2 = Math.sqrt(p2[0] * p2[0] + p2[1] * p2[1]);
                return Double.compare(distance1, distance2);
            }
        });
        for (int[] point : points) {
            pq.offer(point);
        }
        int[][] res = new int[k][2];
        for (int i = 0; i < k; i++) {
            res[i] = pq.poll();
        }
        return res;
    }
}
