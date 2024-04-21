class Solution {
    public String removeStars(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '*') {
                stack.pop();
            }
            else {
                stack.add(c);
            }
        }
        char[] arr = new char[stack.size()];
        for (int i = arr.length - 1; i >=0; i--) {
            arr[i] = stack.pop();
        }
        return new String(arr);
    }
}
