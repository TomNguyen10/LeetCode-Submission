class Solution {
    public int findDuplicate(int[] nums) {
        boolean ans[] = new boolean[nums.length];
        for(int i=0; i<nums.length; i++){
            if(!ans[nums[i]]){
                ans[nums[i]] = true;
            } else {
                return nums[i];
            }
        }
        return 0;
    }
}
