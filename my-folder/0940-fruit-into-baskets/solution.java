class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer, Integer> map = new HashMap<>();
        int left = 0;
        int length = 0;
        int max = 0;
        for (int right = 0; right < fruits.length; right++) {
            if (!map.containsKey(fruits[right])) {
                map.put(fruits[right], 0);
            }
            int idx = map.get(fruits[right]);
            map.put(fruits[right], idx+1);
            length++;
            while (map.size() > 2) {
                int cur = map.get(fruits[left]);
                map.put(fruits[left], cur-1);
                length--;
                if (map.get(fruits[left]) == 0) {
                    map.remove(fruits[left]);
                }
                left++;
            }
            max = Math.max(max, length);
        }

        return max;
    }
}
