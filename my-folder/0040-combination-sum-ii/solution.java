class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
       List<List <Integer>> res = new ArrayList<>();
       Arrays.sort(candidates);
       backtrack(candidates, target, res, new ArrayList<>(), 0);
       return res;
    }

    private void backtrack (int[] candidates, int target, List<List<Integer>> res, List<Integer> temp, int start) {
        if (target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }
        if (target < 0) return;
        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i-1]) continue;
            temp.add(candidates[i]);
            backtrack(candidates, target - candidates[i], res, temp, i+1);
            temp.remove((temp.size() - 1));
        }
    }
}
