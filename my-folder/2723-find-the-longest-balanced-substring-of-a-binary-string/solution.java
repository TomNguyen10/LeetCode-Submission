class Solution {
    public int findTheLongestBalancedSubstring(String s) {
        int max = 0;
        String temp = "01";
        while(temp.length() <= s.length()) {
            if (s.contains(temp)) {
                max = temp.length();
            }
            temp = "0" + temp +"1";
        }
        return max;
    }
}
