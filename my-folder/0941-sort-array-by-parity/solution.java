class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] ans = new int[nums.length];
        int left = 0;
        int right = nums.length - 1;
        int i = 0;
        while (i < nums.length) {
            if (nums[i] % 2 == 0) {
                ans[left++] = nums[i];
            }
            else {
                ans[right--] = nums[i];
            }
            i++;
        }
        return ans;
    }
}
