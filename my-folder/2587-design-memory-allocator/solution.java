class Allocator {

    private int[] memory;
    private Map<Integer, List<int[]>> allocations;

    public Allocator(int n) {
        memory = new int[n];
        allocations = new HashMap<>();
    }
    
    public int allocate(int size, int mID) {
        for (int i = 0; i <= memory.length - size; i++) {
            boolean isFree = true;
            for (int j = i; j < i + size; j++) {
                if (memory[j] != 0) {
                    isFree = false;
                    break;
                }
            }
            if (isFree) {
                for (int j = i; j < i + size; j++) {
                    memory[j] = mID;
                }
                allocations.putIfAbsent(mID, new ArrayList<>());
                allocations.get(mID).add(new int[]{i, size});
                return i;
            }
        }
        return -1;
    }
    
    public int free(int mID) {
        List<int[]> blocks = allocations.getOrDefault(mID, new ArrayList<>());
        int freedUnits = 0;
        for (int[] block : blocks) {
            int start = block[0];
            int size = block[1];
            for (int i = start; i < start + size; i++) {
                if (memory[i] == mID) {
                    memory[i] = 0;
                    freedUnits++;
                }
            }
        }
        allocations.remove(mID);
        return freedUnits;
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * Allocator obj = new Allocator(n);
 * int param_1 = obj.allocate(size,mID);
 * int param_2 = obj.free(mID);
 */
