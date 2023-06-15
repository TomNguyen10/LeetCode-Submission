class TimeMap {

    private HashMap<String, ArrayList<Pair<String, Integer>>> map;

    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (!map.containsKey(key)) map.put(key, new ArrayList<>());
        map.get(key).add(new Pair(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if (!map.containsKey(key)) return "";
        ArrayList<Pair<String, Integer>> list = map.get(key);
        int left = 0;
        int right = list.size() - 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (list.get(mid).getValue() <= timestamp) left = mid; else right = mid - 1;
        }
        
        return list.get(left).getValue() <= timestamp
            ? list.get(left).getKey()
            : "";

    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
