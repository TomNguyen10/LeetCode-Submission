class Solution {
  public int[] getSumAbsoluteDifferences(int[] nums) {
    int[] res = new int[nums.length];
    int[] prefixSum = new int[nums.length + 1];
    for (int i = 0; i < nums.length; i++) {
      prefixSum[i+1] = prefixSum[i] + nums[i];
    }
    for (int i = 0; i < nums.length; i++) {
      res[i] = i * nums[i] - prefixSum[i] + (prefixSum[nums.length] - prefixSum[i] - (nums.length - i) * nums[i]);
    }
    return res;
  }
}
