class Solution {
    List<List<Integer>> combinations = new ArrayList<>();
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> list = new ArrayList<>();
        backtrack(list, 1, n, k);
        return combinations;
    }
    
    private void backtrack(List<Integer> list, int start, int n, int k) {
        if (list.size() == k) {
            combinations.add(new ArrayList<Integer>(list));
            return;
        }
        
        for (int i = start; i <= n; i++) {
            list.add(i);
            backtrack(list, i + 1, n, k);
            list.remove(list.size() - 1);
        }
    }
}
