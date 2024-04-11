class Solution {
    public int minAddToMakeValid(String s) {
        int res = 0;
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            }
            else if (c == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
                else {
                    res += 1;
                }
            }
        }
        res += stack.size();
        return res;
    }
}
