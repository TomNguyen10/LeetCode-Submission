class Solution {
    public int maxRepeating(String sequence, String word) {
        StringBuilder sb = new StringBuilder();
        int count = 0;
        while (sb.length() <= sequence.length()) {
            sb.append(word);
            if (sequence.contains(sb)) count++;
        }
        return count;
    }
}
