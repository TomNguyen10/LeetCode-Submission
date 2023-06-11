class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i : nums) set.add(i);

        int max = 0;
        for (int i : set) {
            if (!set.contains(i-1)) {
                int length = 1;
                while (set.contains(i+length)) {
                    length++;
                }
                max = Math.max(max, length);
            }
        }

        return max;
    }
}
