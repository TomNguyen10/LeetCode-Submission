class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];
        for (int i = 0; i < word1.length(); i++) {
            freq1[word1.charAt(i) - 'a']++;
            freq2[word2.charAt(i) - 'a']++;
        }
        for (int i = 0; i< 26; i++) {
            if ((freq1[i] == 0 && freq2[i] !=0) || (freq1[i] != 0 && freq2[i] ==0)) {
                return false;
            }
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            int count1 = map.getOrDefault(freq1[i], 0);
            map.put(freq1[i], count1+1);
            int count2 = map.getOrDefault(freq2[i], 0);
            map.put(freq2[i], count2-1);
        }
        for (int i : map.values()) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
}
