class Solution {
    public int minSteps(String s, String t) {
        int[] alphabet = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int pos = s.charAt(i) - 'a';
            alphabet[pos]++;
        }
        for (int i = 0; i < t.length(); i++) {
            int pos = t.charAt(i) - 'a';
            alphabet[pos]--;
        }

        int count = 0;
        for (int num : alphabet) {
            count += Math.abs(num-0);
        }

        return count;
    }
}
