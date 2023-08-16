class Solution {
    public String decodeString(String s) {
        Stack<Integer> nums = new Stack<>();
        Stack<StringBuilder> str = new Stack<>();
        StringBuilder res = new StringBuilder();
        int num = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }
            else if (c == '[') {
                nums.push(num);
                num = 0;
                str.push(res);
                res = new StringBuilder();
            }
            else if (c == ']') {
                int i = nums.pop();
                StringBuilder prevStr = str.pop();
                res = prevStr.append(res.toString().repeat(i));
            }
            else {
                res.append(c);
            }
            
        }
        return res.toString();
    }
}
