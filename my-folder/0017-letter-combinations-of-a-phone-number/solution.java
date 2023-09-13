class Solution {
  public List<String> letterCombinations(String digits) {
    List<String> res = new ArrayList<>();
    if (digits.isEmpty()) return res;
    HashMap<Character, String> map = new HashMap<Character, String> ();
    map.put('2', "abc");
    map.put('3', "def");
    map.put('4', "ghi");
    map.put('5', "jkl");
    map.put('6', "mno");
    map.put('7', "pqrs");
    map.put('8', "tuv");
    map.put('9', "wxyz");

    backtrack(res, "", digits, 0, map);
    return res;
  }

  private void backtrack(List<String> res, String cur, String digits, int index, Map<Character, String> map) {
    if (index == digits.length()) {
      res.add(cur);
      return;
    }
    char currentDigit = digits.charAt(index);
    String letter = map.get(currentDigit);

    for (int i = 0; i < letter.length(); i++) {
      backtrack(res, cur + letter.charAt(i), digits, index+1, map);
    }
  }
}
