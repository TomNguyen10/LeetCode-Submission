class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 != 0) return false;
        Stack<Character> st = new Stack<>();
        char top;
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') st.push(c);
            else {
                if (st.isEmpty()) return false;
                else {
                    top = st.pop();
                    switch (c) {
                        case ')':
                            if (top != '(') return false;
                            break;
                        case ']':
                            if (top != '[') return false;
                            break;
                        case '}':
                            if (top != '{') return false;
                            break;
                    }
                }
            }
        }
        if (!st.isEmpty()) return false;
        return true;
    }
}
