class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // Using binary search to check the minimum rate of eating
        // The min will be 1 and the max is the maximum pile in the piles array
        // Calculate the middle value and run a simulation for that to check if it is satisfy or not
        // Return the minimum value
        int max = 0;
        int min = 1;
        for (int pile : piles) {
            max = Math.max(max, pile);
        }
        int res = max;
        while (min < max) {
            int mid = min + (max - min)/2;
            int hours = 0;
            for (int pile : piles) {
                hours += Math.ceil((double) pile / mid);
            }
            if (hours <= h) {
                res = mid;
                max = mid;
            }
            else {
                min = mid+1;
            }
        }
        return res;
    }
}
