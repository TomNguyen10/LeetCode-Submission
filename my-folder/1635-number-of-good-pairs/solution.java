class Solution {
    public int numIdenticalPairs(int[] nums) {
        int count = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            if (!map.containsKey(i)) {
                map.put(i, 1);
            }
            else {
                int val = map.get(i);
                count += val;
                map.put(i, val+1);
            }
        }
        return count;
    }
}
