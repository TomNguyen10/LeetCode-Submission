class SmallestInfiniteSet {

    private int cur;
    private Set<Integer> set;

    public SmallestInfiniteSet() {
        cur = 1;
        set = new TreeSet<>();
    }
    
    public int popSmallest() {
        if (!set.isEmpty()) {
            int res = set.iterator().next();
            set.remove(res);
            return res;
        }
        else {
            return cur++;
        }
    }
    
    public void addBack(int num) {
        if (cur > num) {
            set.add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */
