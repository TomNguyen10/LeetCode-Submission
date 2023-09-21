class Solution {
    public int findValueOfPartition(int[] nums) {
        int min = Integer.MAX_VALUE;
        Arrays.sort(nums);
        for (int i = 1; i < nums.length; i++) {
            min = Math.min(nums[i]-nums[i-1], min);
        }
        return min;
    }
}
