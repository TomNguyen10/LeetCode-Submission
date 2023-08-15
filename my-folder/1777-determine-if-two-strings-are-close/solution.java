class Solution {
    public boolean closeStrings(String word1, String word2) {
        int[] H1 = new int[26];
        int[] H2 = new int[26];
        
        for (char c : word1.toCharArray()) {
            H1[c - 'a']++;
        }
        for (char c : word2.toCharArray()) {
            H2[c - 'a']++;
        }
        
        for (int i = 0; i < 26; ++i) {
            if ((H1[i] != 0 && H2[i] == 0) || (H1[i] == 0 && H2[i] != 0)) {
                return false;
            }
        }
        
        Map<Integer, Integer> frequencyOfFrequencyHash = new HashMap<>();
        for (int freq : H1) {
            frequencyOfFrequencyHash.put(freq, frequencyOfFrequencyHash.getOrDefault(freq, 0) + 1);
        }
        for (int freq : H2) {
            frequencyOfFrequencyHash.put(freq, frequencyOfFrequencyHash.getOrDefault(freq, 0) - 1);
        }
        
        for (int freqCount : frequencyOfFrequencyHash.values()) {
            if (freqCount != 0) {
                return false;
            }
        }
        
        return true;
    }
}
