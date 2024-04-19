class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> list = new ArrayList<>();
        boolean inserted = false;
        for (int[] interval : intervals) {
            if (interval[1] < newInterval[0]) {
                list.add(interval);
            }
            else if (interval[0] > newInterval[1]) {
                if (inserted == false) {
                    list.add(newInterval);
                    inserted = true;
                }
                list.add(interval);
            }
            else {
                newInterval[0] = Math.min(newInterval[0], interval[0]);
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            }
        }

        if (inserted == false) {
            list.add(newInterval);
        }
        int[][]res = new int[list.size()][2];
        for (int i = 0; i < list.size(); i++) {
            int[] arr = list.get(i);
            res[i] = new int[]{arr[0], arr[1]};
        }
        return res;
    }
}
