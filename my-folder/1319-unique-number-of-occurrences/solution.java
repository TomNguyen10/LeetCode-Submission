class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : arr) {
            int count = map.getOrDefault(i, 0);
            map.put(i, count+1);
        }
        Set<Integer> set = new HashSet<>();
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int value = entry.getValue();
            if (set.contains(value)) {
                return false;
            }
            set.add(value);
        }
        return true;
    }
}
