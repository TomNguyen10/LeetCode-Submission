class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int left, right;
        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i-1])) {
                left = i+1;
                right = nums.length-1;
                while (left < right) {
                    if (nums[left] + nums[right] == nums[i]*-1) {
                        List<Integer> put = new ArrayList<>();
                        put.add(nums[i]);
                        put.add(nums[left]);
                        put.add(nums[right]);
                        res.add(put);
                        while (left < right && nums[left] == nums[left + 1]) {
                            left++;
                        }
                        while (left < right && nums[right] == nums[right - 1]) {
                            right--;
                        }
                        left++;
                        right--;
                    }
                    else if (nums[left] + nums[right] > nums[i]*-1) {
                        right--;
                    }
                    else {
                        left++;
                    }
                }
            }
        }
        return res;
    }
}
