class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        for (char number : num.toCharArray()) {
            while (!stack.isEmpty() && stack.peek() > number && k > 0) {
                stack.pop();
                k--;
            }
            stack.push(number);
        }
        while (k > 0) {
            stack.pop();
            k--;
        }
        ArrayList<Character> res = new ArrayList<>(stack);
        while (!res.isEmpty() && res.get(0) == '0') {
            res.remove(0);
        }
        StringBuilder sb = new StringBuilder();
        for (char c : res) {
            sb.append(c);
        }
        String ans = sb.toString();
        if (ans.equals("")) {
            return "0";
        }
        return ans;
    }
}
