class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        for (int stone : stones) {
            pq.offer(stone);
        }
        while (pq.size() > 1) {
            int s1 = pq.poll();
            int s2 = pq.poll();
            int sub = s1 - s2;
            if (sub > 0) {
                pq.offer(sub);
            }
        }
        if (pq.isEmpty()) {
            return 0;
        }
        return pq.poll();
    }
}
