class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) {
            int current = count.getOrDefault(num, 0);
            count.put(num, current+1);
        }
        List<Integer>[] bucket = new ArrayList[nums.length+1];
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            Integer key = entry.getKey();
            Integer value = entry.getValue();
            if (bucket[value] == null) bucket[value] = new ArrayList<Integer>();
            bucket[value].add(key);
        }
        int[] res = new int[k];
        for (int i = nums.length; i > -1; i--) {
            if (bucket[i] != null) {
                for (int z : bucket[i]) {
                    res[--k] = z;
                    if (k == 0) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
}
