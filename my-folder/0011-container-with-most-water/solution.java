class Solution {
    public int maxArea(int[] height) {
        int res = 0;
        int left = 0;
        int right = height.length - 1;
        while (left < right) {
            int w = right - left;
            int h = Math.min(height[right], height[left]);
            int water = w*h;
            res = Math.max(res, water);
            if (height[left] >= height[right]) {
                right--;
            }
            else {
                left++;
            }
        } 
        return res;
    }
}
