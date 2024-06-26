class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i] = new int[]{nums2[i], nums1[i]};
        }  
        Arrays.sort(pairs, (a,b) -> b[0] - a[0]);
        PriorityQueue<Integer> pq = new PriorityQueue<>(k, (a, b) -> a - b);
        long res = 0;
        long sum = 0;
        for (int[] pair : pairs) {
            pq.add(pair[1]);
            sum += pair[1];
            if (pq.size() > k) {
                sum -= pq.poll();
            }
            if (pq.size() == k) {
                res = Math.max(res, (sum * pair[0]));
            }
        }
        return res;
    }
}
