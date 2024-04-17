class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            //Check if the left half is sorted
            if (nums[left] <= nums[mid]) {
                //If the left half is sorted:
                //If the target is within the sorted left half,
                //adjust the right pointer to search the left half.
                //Otherwise, adjust the left pointer to search the right half.
                if (target > nums[mid] || target < nums[left]) {
                    left = mid + 1;
                }
                else {
                    right = mid - 1;
                }
            }
            //If the right half is sorted
            else {
                //If the right half is sorted:
                //If the target is within the sorted right half,
                //adjust the left pointer to search the right half.
                //Otherwise, adjust the right pointer to search the left half.
                if (target < nums[mid] || target > nums[right]) {
                    right = mid - 1;
                }
                else {
                    left = mid + 1;
                }
            }
        } 
        return -1;
    }
}
