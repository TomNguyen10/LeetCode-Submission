class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int left = 0;
        int right = 0;
        int res = 0;
        while (right < s.length()) {
            if (!set.contains(s.charAt(right))) {
                set.add(s.charAt(right));
                res = Math.max(res, right - left + 1);
                right++;
            }
            else {
                set.remove(s.charAt(left));
                left++;
            }
        }
        return res;
    }
}
