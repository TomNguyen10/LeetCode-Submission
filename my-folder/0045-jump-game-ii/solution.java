class Solution {
    public int jump(int[] nums) {
        int jump = 0;
        int curEnd = 0;
        int curFar = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            curFar = Math.max(curFar, i + nums[i]);
            if (i == curEnd) {
                jump++;
                curEnd = curFar;
            }
        }
        return jump;
    }
}
