class Solution {
    public int longestSubarray(int[] nums) {
        int i = 0;
        int j;
        int k = 1;
        for (j = 0; j < nums.length; j++) {
            if (nums[j] == 0) k--;
            if (k < 0 && nums[i++] == 0) k++;
        }
        return j - i - 1;
    }
}
