class Solution {
    public String reverseWords(String s) {
        String[] words = s.split("\\s+");
        StringBuilder res = new StringBuilder();
        for (String word : words) {
            StringBuilder rev = new StringBuilder(word);
            rev.reverse();
            res.append(rev).append(" ");
        }
        return res.toString().trim();
    }
}
