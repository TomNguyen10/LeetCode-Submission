class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(k, n, res, new ArrayList<Integer>(), 1);
        return res;
    }

    private void backtrack(int k, int n, List<List<Integer>> res, List<Integer> comb, int start) {
        if (comb.size() == k && n == 0) {
            List<Integer> list = new ArrayList<Integer>(comb);
            res.add(list);
            return;
        }
        for (int i = start; i <= 9; i++) {
            comb.add(i);
            backtrack(k, n-i, res, comb, i+1);
            comb.remove(comb.size() - 1);
        }
    }
}
