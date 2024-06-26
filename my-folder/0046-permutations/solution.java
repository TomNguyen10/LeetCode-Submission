class Solution {

    List<List<Integer>> res = new ArrayList<>();
 
    public List<List<Integer>> permute(int[] nums) {
        backtrack(nums, new ArrayList<>());
        return res;
    }

    private void backtrack(int[] nums, List<Integer> temp) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if(temp.contains(nums[i])) {
                continue;
            }   
            temp.add(nums[i]);
            backtrack(nums, temp);
            temp.remove(temp.size() - 1);
        }
    }

}
