class Solution {
    public int characterReplacement(String s, int k) {
        int res = 0;
        int max = 0;
        int[] count = new int[26];
        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            count[s.charAt(right) - 'A']++;
            max = Math.max(max, count[s.charAt(right) - 'A']);
            if (right - left + 1 - max > k) {
                count[s.charAt(left) - 'A']--;
                left++;
            }
            res = Math.max(res, right - left + 1);
        }
        return res;
    }
}
