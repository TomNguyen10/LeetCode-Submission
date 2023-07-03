class Solution {
    public String digitSum(String s, int k) {
        if (s.length() <= k) return s;

        StringBuilder res = new StringBuilder();
        int sum = 0;
        for (int i = 1; i <= s.length(); i++) {
            sum += s.charAt(i-1) - '0';
            if (i % k == 0 || i == s.length()) {
                res.append(sum);
                sum = 0;
            }
        }
        return digitSum(res.toString(), k);
    }
}
