class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            if (!map.containsKey(i)) map.put(i, 1);
            else {
                int val = map.get(i);
                map.put(i, val+1);
            }
        }

        ArrayList<Integer>[] bucket = new ArrayList[nums.length+1];
        for (int key : map.keySet()) {
            int value = map.get(key);
            if (bucket[value] == null) bucket[value] = new ArrayList<Integer>();
            bucket[value].add(key);
        }

        int[] res = new int[k];
        int count = 0;
        for (int i = nums.length; i >= 0; i--) {
            if (bucket[i] != null) {
                for (int r : bucket[i]) {
                    res[count++] = r;
                    if (count == k) return res;
                }
            }
        }

        return res;
    }
}
