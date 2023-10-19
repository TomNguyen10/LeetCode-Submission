/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int n = mountainArr.length();
        int peak = 0;
        int left = 0;
        int right = n - 1;
        while (left < right) {
            int middle = (left + right) / 2;
            if (mountainArr.get(middle) < mountainArr.get(middle + 1)) {
                left = peak = middle + 1;
            }
            else {
                right = middle;
            }
        }
        left = 0;
        right = peak;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (mountainArr.get(middle) < target) {
                left = middle + 1;
            }
            else if (mountainArr.get(middle) > target) {
                right = middle - 1;
            }
            else {
                return middle;
            }
        }
        left = peak;
        right = n - 1;
        while (left <= right) {
            int middle = (left + right) / 2;
            if (mountainArr.get(middle) < target) {
                right = middle - 1;
            }
            else if (mountainArr.get(middle) > target) {
                left = middle + 1;
            }
            else {
                return middle;
            }
        }
        return -1;
    }
}
