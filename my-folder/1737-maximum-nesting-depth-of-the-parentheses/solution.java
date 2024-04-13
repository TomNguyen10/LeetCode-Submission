class Solution {
    public int maxDepth(String s) {
        int current = 0;
        int res = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') {
                current++;
                res = Math.max(res, current);
            }
            else if (c == ')') {
                current--;
            }
        }
        return res;
    }
}
