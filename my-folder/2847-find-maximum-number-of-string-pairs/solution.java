class Solution {
    public int maximumNumberOfStringPairs(String[] words) {
        int count = 0;
        Set<String> set = new HashSet<>();
        for (String word : words) {
            StringBuilder sb = new StringBuilder(word);
            sb.reverse();
            if (set.contains(sb.toString())) {
                count++;
            }
            else {
                set.add(word);
            }
        }
        return count;
    }
}
