class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int maxLeft = height[0];
        int maxRight = height[n-1];
        int left = 1;
        int right = n-2;
        int water = 0;
        int trap = 0;
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
                trap += water;
            }
        }
        return trap;
    }
}
