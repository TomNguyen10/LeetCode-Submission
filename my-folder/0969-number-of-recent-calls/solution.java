class RecentCounter {

    List<Integer> pings;

    public RecentCounter() {
        pings = new ArrayList<>();
    }
    
    public int ping(int t) {
        pings.add(t);
        int count = 0;
        for (int i = 0; i < pings.size(); i++) {
            if (pings.get(i) >= t - 3000) {
                count ++;
            }
        }
        return count;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
