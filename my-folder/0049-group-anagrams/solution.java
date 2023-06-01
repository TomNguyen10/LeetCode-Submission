class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, ArrayList<String>> res = new HashMap<>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String val = String.valueOf(ca);
            if (!res.containsKey(val)) res.put(val, new ArrayList<>());
            res.get(val).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
