class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int left = 1;
        int right = n - 2;
        int maxLeft = height[0];
        int maxRight = height[n - 1];
        int water = 0;
        int res = 0;
        while (left <= right) {
            if (maxLeft <= maxRight) {
                water = maxLeft - height[left];
                maxLeft = Math.max(maxLeft, height[left]);
                left++;
            }
            else {
                water = maxRight - height[right];
                maxRight = Math.max(maxRight, height[right]);
                right--;
            }
            if (water > 0) {
                res += water;
            }
        }
        return res;
    }
}
