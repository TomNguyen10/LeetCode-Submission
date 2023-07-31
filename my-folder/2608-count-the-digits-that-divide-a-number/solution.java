class Solution {
    public int countDigits(int num) {
        int clone = num;
        int count = 0;
        while (clone > 0) {
            int divide = clone % 10;
            if (num % divide == 0) count++;
            clone /= 10;
        }
        return count;
    }
}
