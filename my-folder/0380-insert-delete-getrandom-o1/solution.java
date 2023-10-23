class RandomizedSet {

    java.util.Random rand = new java.util.Random();
    Map<Integer, Integer> map;
    List<Integer> list;

    public RandomizedSet() {
        map = new HashMap<>();
        list = new ArrayList<>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        map.put(val, list.size());
        list.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) return false;
        int location = map.get(val);
        if (location < list.size() - 1) {
            int last = list.get(list.size() - 1);
            list.set(location, last);
            map.put(last, location);
        }
        map.remove(val);
        list.remove(list.size() - 1);
        return true;
    }
    
    public int getRandom() {
        int random = rand.nextInt(list.size());
        return list.get(random);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
