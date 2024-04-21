class Solution {
    public String decodeString(String s) {
        StringBuilder res = new StringBuilder();
        Stack<Integer> si = new Stack<>();
        Stack<StringBuilder> ss = new Stack<>();
        int num = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }
            else if (c == '[') {
                si.push(num);
                num = 0;
                ss.push(res);
                res = new StringBuilder();
            }
            else if (c == ']') {
                int i = si.pop();
                StringBuilder prev = ss.pop();
                res = prev.append(res.toString().repeat(i));
            }
            else {
                res.append(c);
            }
        }
        return res.toString();
    }
}
