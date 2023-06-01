class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i : nums) {
            if (!map.containsKey(i)) {
                map.put(i, 1);
            }
            else {
                int val = map.get(i);
                map.put(i, val+1);
            }
        }

        ArrayList<Integer>[] bucket = new ArrayList[nums.length + 1];
        int[] res = new int[k];

        for (Integer key : map.keySet()) {
            int value = map.get(key);
            if (bucket[value] == null) {
                bucket[value] = new ArrayList<Integer>();
            }
            bucket[value].add(key);
        }

        int idx = 0;

        for (int i = nums.length; i >= 0; i--)
            if (bucket[i] != null)
                for (int val : bucket[i]){
                    res[idx++] = val;
                    if(idx == k)
                        return res;
                }
        return res;
    }
}
