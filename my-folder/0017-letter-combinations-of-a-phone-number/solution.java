class Solution {

    List<String> res = new ArrayList<>(); 
    Map<Character, String> map = new HashMap<>();

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return res;
        }
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        backtrack("", 0, digits);
        return res;
    }

    private void backtrack(String current, int index, String digits) {
        if (index == digits.length()) {
            res.add(current);
            return;
        }
        String letters = map.get(digits.charAt(index));
        for (int i = 0; i < letters.length(); i++) {
            backtrack(current + letters.charAt(i), index+1, digits);
        }
    }
}
