class Solution {
    public int pivotIndex(int[] nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        int current = 0;
        for (int i = 0; i < nums.length; i++) {
            if ((double)current == (double)(total - nums[i])/2) {
                return i;
            }
            current += nums[i];
        }
        return -1;
    }
}
