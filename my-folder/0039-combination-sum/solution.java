class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), target, 0, candidates);
        return res;
    }

    private void backtrack(List<List<Integer>> res, List<Integer> temp, int target, int index, int[] nums) {
        if (target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }
        if (target < 0 || index >= nums.length) {
            return;
        }
        temp.add(nums[index]);
        backtrack(res, temp, target - nums[index], index, nums);
        temp.remove(temp.size() - 1);
        backtrack(res, temp, target, index+1, nums);
    }

}

