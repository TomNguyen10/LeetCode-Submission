class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Arrays.sort(deck);
        int[] res = new int[deck.length];
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < deck.length; i++) {
            queue.add(i);
        }
        for (int i = 0; i < deck.length; i++) {
            res[queue.poll()] = deck[i];
            queue.add(queue.poll());
        }
        return res;
    }
}
