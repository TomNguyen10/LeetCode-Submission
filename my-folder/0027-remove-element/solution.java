class Solution {
    public int removeElement(int[] nums, int val) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                int temp = nums[res];
                nums[res] = nums[i];
                nums[i] = temp;
                res++; 
            }
        }
        return res;
    }
}
