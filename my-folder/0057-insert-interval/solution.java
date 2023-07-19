import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> merged = new ArrayList<>();
        
        int i = 0;
        int n = intervals.length;
        
        // Add intervals before newInterval that end before newInterval starts
        while (i < n && intervals[i][1] < newInterval[0]) {
            merged.add(intervals[i]);
            i++;
        }
        
        // Merge intervals that overlap with newInterval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
            i++;
        }
        
        // Add the merged newInterval
        merged.add(newInterval);
        
        // Add the remaining intervals
        while (i < n) {
            merged.add(intervals[i]);
            i++;
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
}

