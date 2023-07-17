class Solution {
    public String reformat(String s) {
        List<Character> letters = new ArrayList<>();
        List<Character> digits = new ArrayList<>();

        for (char ch : s.toCharArray()) {
            if (Character.isLetter(ch)) letters.add(ch);
            else  digits.add(ch);
        }

        int lettersCount = letters.size();
        int digitsCount = digits.size();

        if (Math.abs(lettersCount - digitsCount) > 1) return "";
        
        List<Character> longerList;
        List<Character> shorterList;

        if (lettersCount > digitsCount) {
            longerList = letters;
            shorterList = digits;
        } else {
            longerList = digits;
            shorterList = letters;
        }

        StringBuilder sb = new StringBuilder();
        
        while (!longerList.isEmpty()) {
            sb.append(longerList.get(0));
            longerList.remove(0);
            if (!shorterList.isEmpty()) {
                sb.append(shorterList.get(0));
                shorterList.remove(0);
            }
        }

        return sb.toString();
    }

}
