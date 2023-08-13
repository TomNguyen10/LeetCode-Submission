class Solution {
    public boolean isSubsequence(String s, String t) {
        int pointer1 = 0;
        for (int pointer2 = 0; pointer2 < t.length(); pointer2++) {
            if (pointer1 < s.length() && s.charAt(pointer1) == t.charAt(pointer2)) {
                pointer1++;
            }
        }
        return pointer1 == s.length();
    }
}
