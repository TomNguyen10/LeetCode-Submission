class Solution {
    public int minimumCardPickup(int[] cards) {
        int min = cards.length+1;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < cards.length; i++) {
            if (map.containsKey(cards[i])) {
                int val = i - map.get(cards[i]);
                min = Math.min(val, min);
            }
            map.put(cards[i], i);
        }
        if (min == cards.length+1) return -1;
        return min+1;
    }
}
