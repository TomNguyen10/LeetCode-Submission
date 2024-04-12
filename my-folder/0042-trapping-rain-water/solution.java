class Solution {
    public int trap(int[] height) {
        if (height.length < 2) {
            return 0;
        }

        int maxLeft = height[0];
        int maxRight = height[height.length - 1];
        int right = height.length - 2;
        int left = 0;
        int res = 0;
        int water = 0;

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
