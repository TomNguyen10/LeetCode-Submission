class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0;
        int right = 0;
        int minLength = nums.length+1;
        int currSum = 0;
        while (right < nums.length) {
            currSum += nums[right];
            while (currSum >= target) {
                minLength = Math.min(minLength, right - left + 1);
                currSum -= nums[left];
                left++;
            }
            right++;
        }

        if (minLength == nums.length+1) return 0;
        return minLength;
    }
}
