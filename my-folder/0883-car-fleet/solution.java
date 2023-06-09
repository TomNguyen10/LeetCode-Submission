class Solution {
    public int carFleet(int target, int[] position, int[] speed) {//tc = O(nlogn) sc = O(n)
        if (position.length == 1 || position.length == 0) return position.length;
        
        // number of fleet:
        int numberOfCarFleet = position.length;

        float [] arraytime = new float[target];

        for (int i = 0; i < position.length; i++) {
            arraytime[position[i]] = (float)(target - position[i]) / speed[i];
        }

        float previousTime = 0;
        int res = 0;

        for (int i = target-1; i >=0 ; i--) {
            float currentTime = arraytime[i];

            if (currentTime > previousTime) {
                previousTime = currentTime;
                res++;
            }
        }
        return res;
    }
}
