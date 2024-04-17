class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtrack(res, "", n, n);
        return res;
    }

    void backtrack(List<String> list, String current, int open, int close) {
        if (open == 0 && close == 0) {
            list.add(current);
            return;
        }
        if (open > 0) {
            backtrack(list, current+'(', open-1, close);
        }
        if (close > open) {
            backtrack(list, current + ')', open, close - 1);
        }
    }
}
