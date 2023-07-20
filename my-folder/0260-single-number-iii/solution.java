class Solution {
    public int[] singleNumber(int[] nums) {
       int xorResult = 0;
        for (int num : nums) {
            xorResult ^= num;
        }

        int rightmostSetBit = xorResult & -xorResult;

        int group1 = 0;
        int group2 = 0;
        for (int num : nums) {
            if ((num & rightmostSetBit) != 0) {
                group1 ^= num;
            } else {
                group2 ^= num;
            }
        }

        return new int[]{group1, group2}; 
    }
}
