class Solution {
    public int findMinDifference(List<String> timePoints) {
        Collections.sort(timePoints);
        int min = 1440;
        for (int i = 1; i < timePoints.size(); i++) {
            int time1 = cal(timePoints.get(i-1));
            int time2 = cal(timePoints.get(i));
            min = Math.min(time2 - time1, min);
            if (min == 0) return 0;
        }

        int first = cal(timePoints.get(0));
        int last = cal(timePoints.get(timePoints.size() - 1));
        min = Math.min(first + 1440 - last, min);
        return min;
    }

    private int cal(String time) {
        String[] t = time.split(":");
        int h = Integer.parseInt(t[0]);
        int m = Integer.parseInt(t[1]);
        return h*60 + m;
    }
}
