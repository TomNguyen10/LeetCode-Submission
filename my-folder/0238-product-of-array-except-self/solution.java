class Solution {
    public int[] productExceptSelf(int[] nums) {
        int pre = 1;
        int suf = 1;
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        for (int i = 0; i < prefix.length; i++) {
            prefix[i] = pre;
            pre *= nums[i];
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            suffix[i] = suf;
            suf *= nums[i];
        }
        int[] res = new int[nums.length];
        for (int i = 0; i < res.length; i++) {
            res[i] = prefix[i] * suffix[i];
        }
        return res;
    }
}
