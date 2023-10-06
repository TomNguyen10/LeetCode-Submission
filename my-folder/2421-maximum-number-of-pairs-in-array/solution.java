class Solution {
    public int[] numberOfPairs(int[] nums) {
        int pairs = 0;
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                pairs++;
                set.remove(nums[i]);
            }
            else {
                set.add(nums[i]);
            }
        }
        int[] res = new int[2];
        res[0] = pairs;
        res[1] = set.size();
        return res;
    }
}
