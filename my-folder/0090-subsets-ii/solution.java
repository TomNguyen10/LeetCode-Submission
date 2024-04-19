class Solution {

    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        backtrack(nums, 0, new ArrayList<>());
        return new ArrayList<>(res);
    }

    private void backtrack(int[] nums, int index, List<Integer> temp) {
        res.add(new ArrayList<>(temp));
        for (int i = index; i < nums.length; i++) {
            if (i > index && nums[i] == nums[i-1]) {
                continue;
            }
            temp.add(nums[i]);
            backtrack(nums, i + 1, temp);
            temp.remove(temp.size() - 1);
        }
    }
}
