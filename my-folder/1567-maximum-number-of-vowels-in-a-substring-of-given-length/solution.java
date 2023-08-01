class Solution {
    public int maxVowels(String s, int k) {
        int maxVowels = 0;
        int currentVowels = 0;
        HashSet<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        for (int i = 0; i < k; i++) {
            if (vowels.contains(s.charAt(i))) {
                currentVowels++;
            }
        }
        maxVowels = Math.max(maxVowels, currentVowels);

        for (int i = k; i < s.length(); i++) {
            char leftChar = s.charAt(i - k); 
            char rightChar = s.charAt(i);    

            if (vowels.contains(leftChar)) {
                currentVowels--;
            }
            if (vowels.contains(rightChar)) {
                currentVowels++;
            }

            maxVowels = Math.max(maxVowels, currentVowels);
        }

        return maxVowels;

    }
}
