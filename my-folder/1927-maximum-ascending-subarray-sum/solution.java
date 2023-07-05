class Solution {
    public int maxAscendingSum(int[] nums) {
        int max = nums[0];
        int left = 0;
        int right = 1;
        int sum = nums[0];
        while (right < nums.length) {
            if(nums[right] > nums[right - 1]) {
                sum += nums[right];
            }
            else {
                sum = nums[right];
                left = right;
            }
            right++;
            if (max < sum) max = sum;
        }

        return max;
    }
}
