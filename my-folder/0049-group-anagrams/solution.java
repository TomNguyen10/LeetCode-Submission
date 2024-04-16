class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String sorted_s = String.valueOf(ca);
            if (!map.containsKey(sorted_s)) {
                map.put(sorted_s, new ArrayList<>());
            }
            map.get(sorted_s).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
