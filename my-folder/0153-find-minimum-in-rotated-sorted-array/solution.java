class Solution {
    public int findMin(int[] nums) {
        // Implement the binary search technique
        // Calculate the midde, if the number in the middle is larger 
        // than the number at the end side, it means that the minimum 
        // is on the right side. Update the left to be the middle + 1
        // Else the minimum is on the left side update the right side to be middle
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int middle = left + (right - left) / 2;
            if (nums[middle] > nums[right]) {
                left = middle + 1;
            }
            else {
                right = middle;
            }
        }
        return nums[left];
    }
}
