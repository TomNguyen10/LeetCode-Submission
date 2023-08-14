class Solution {
    public int pivotIndex(int[] nums) {
        int[] leftSum = new int[nums.length];
        int[] rightSum = new int[nums.length];
        int left = 0, right = 0;
        for (int i = 0; i < nums.length; i++) {
            leftSum[i] += left;
            left += nums[i];
        }
        for (int j = nums.length - 1; j >= 0; j--) {
            rightSum[j] += right;
            right+= nums[j];
        }
        for (int r = 0; r < nums.length; r++) {
            if (leftSum[r] == rightSum[r]) return r;
        }   
        return -1;
    }
}
