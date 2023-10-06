class Solution {
    public int maxVowels(String s, int k) {
        int max = 0;
        int cur = 0;
        Set<Character> set = new HashSet<>();
        set.add('a');
        set.add('e');
        set.add('i');
        set.add('o');
        set.add('u');
        for (int i = 0; i < k; i++) {
            char c = s.charAt(i);
            if (set.contains(c)) {
                cur++;
            }
        }
        max = Math.max(max, cur);
        for (int i = k; i < s.length(); i++) {
            char left = s.charAt(i - k);
            char right = s.charAt(i);
            if (set.contains(left)) {
                cur--;
            }
            if (set.contains(right)) {
                cur++;
            }
            max = Math.max(max, cur);
        }
        return max;
    }
}
