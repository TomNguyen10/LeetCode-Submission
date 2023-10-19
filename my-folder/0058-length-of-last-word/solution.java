class Solution {
    public int lengthOfLastWord(String s) {
        s.trim();
        int res = 0;
        for (String sub : s.split(" ")) {
            res = sub.length();
        }
        return res;
    }
}
