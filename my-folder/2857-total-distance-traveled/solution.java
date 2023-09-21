class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int distance = 0;
        while (mainTank >= 5 && additionalTank >= 1) {
            distance += 50;
            mainTank -= 4;
            additionalTank--;
        }
        return distance + mainTank*10;
    }
}
