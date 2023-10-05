class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            int k = map.getOrDefault(i, 0);
            map.put(i, k+1);
        }
        for (int i : map.keySet()) {
            int k = map.get(i);
            if (k > nums.length/3) {
                res.add(i);
            }
        }
        return res;
    }
}
