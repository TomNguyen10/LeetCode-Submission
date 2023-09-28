class Solution {
    public int maximumCostSubstring(String s, String chars, int[] vals) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < chars.length(); i++) {
            map.put(chars.charAt(i), vals[i]);
        }
        int max = 0;
        int cost = 0;
        for (int i = 0; i < s.length(); i++) {
            char curChar = s.charAt(i);
            if (map.containsKey(curChar)) {
                cost += map.get(curChar);
            }
            else {
                cost += curChar - 'a' + 1;
            }
            if (cost < 0) {
                cost = 0;
            }
            max = Math.max(cost, max);
        }
        return max;
    }
}
