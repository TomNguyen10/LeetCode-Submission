class Solution {
    public void sortColors(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int temp = 0;
        
        while (temp <= right) {
            if (nums[temp] == 0) {
                int store = nums[left];
                nums[left] = nums[temp];
                nums[temp] = store;
                left++;
            }
            else if(nums[temp] == 2) {
                int store = nums[right];
                nums[right] = nums[temp];
                nums[temp] = store;
                right--;
                temp--;
            }
            temp++;
        }
    }
}
