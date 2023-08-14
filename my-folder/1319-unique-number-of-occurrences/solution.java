class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : arr) {
            map.merge(i, 1, Integer::sum);
        }
        Set<Integer> set = new HashSet<>();
        for (int freq : map.values()) {
            if (set.contains(freq)) {
                return false;
            }
            else {
                set.add(freq);
            }
        }
        return true;
    }
}
