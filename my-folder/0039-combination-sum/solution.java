class Solution {   

    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
       List<Integer> temp = new ArrayList<>();
       backtrack(candidates, target, temp, 0);
       return res;
    }

    public void backtrack(int[] candidates, int target, List<Integer> temp, int index) {
        if (target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }
        if (target < 0 || index == candidates.length) {
            return;
        }
        temp.add(candidates[index]);
        backtrack(candidates, target - candidates[index], temp, index);
        temp.remove(temp.get(temp.size() - 1));
        backtrack(candidates, target, temp, index + 1);
    } 
}
