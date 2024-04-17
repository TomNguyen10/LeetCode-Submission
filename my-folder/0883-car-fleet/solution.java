class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        if (position.length == 1 || position.length == 0) {
            return position.length;
        }
        double [] times = new double[target];
        for (int i = 0; i < position.length; i++) {
            times[position[i]] = (double) (target - position[i]) / speed[i];
        }
        double prev = 0;
        int res = 0;
        for (int i = target - 1; i >=0; i--) {
            double current = times[i];
            if (current > prev) {
                prev = current;
                res++;
            }
        }
        return res;
    }
}
