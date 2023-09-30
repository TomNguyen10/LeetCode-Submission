class Solution {
    public boolean find132pattern(int[] nums) {
        if (nums.length <= 2) return false;
        int s3 = Integer.MIN_VALUE;
        Stack<Integer> stack = new Stack<>();
        for (int i = nums.length-1; i >= 0; i--) {
            if (nums[i] < s3) return true;
            else {
                while (!stack.isEmpty() && nums[i] > stack.peek()) {
                    s3 = stack.pop();
                }
            }
            stack.push(nums[i]);
        }
        return false;
    }
}
