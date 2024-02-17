class Solution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
      int ans = 0;
      int pre_sum = 0;
      PriorityQueue<Integer> pq = new PriorityQueue<>();
      for (int i = 1; i < heights.length; i++) {
        int diff = heights[i] - heights[i-1];
        if (diff > 0) {
            if (ladders > 0) {
                pq.offer(diff);
                if (pq.size() > ladders) {
                    pre_sum += pq.poll();
                }
            }
            else {
                pre_sum += diff;
            }
            if (pre_sum > bricks) {
                return ans;
            }
        }
        ans = i;
      }  
      return ans;
    }
}
