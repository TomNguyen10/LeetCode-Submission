class Solution {
    public int trap(int[] height) {
        if (height.length <= 2) return 0;
        int maxLeft = height[0];
        int maxRight = height[height.length - 1];
        int left = 1, right = height.length - 2;
        int water, trap = 0;
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