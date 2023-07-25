class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = words.length;
        boolean[] truth = new boolean[26];
        for (char c : allowed.toCharArray()) {
            truth[c - 'a'] = true;
        }
        for (String word : words) {
            for (char c : word.toCharArray()) {
                if (truth[c - 'a'] == false) {
                    count--;
                    break;
                }
            }
        }
        return count;
    }
}
