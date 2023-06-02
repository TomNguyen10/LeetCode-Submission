class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();

        for (int i : nums) {
            set.add(i);
        }

        int maxLength = 0;
        for (int i : set) {
            if (!set.contains(i-1)) {
                int length = 1;
                while (set.contains(i + length)) {
                    length++;
                }
                maxLength = Math.max(length, maxLength);
            }
        }

        return maxLength;
    }
}
